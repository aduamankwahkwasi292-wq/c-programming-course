#!/usr/bin/env python3
"""
Compile and run every C program in the course, and compare what it prints with the output shown in the text.

    python tools/check_programs.py                 check everything
    python tools/check_programs.py lessons/05*.md  check some files only

What is checked
  * every ```c block that contains main() is compiled with  gcc -Wall -Wextra  and run;
  * if an ```output block follows it, the real output must match it. For interactive programs the input comes
    from a marker such as <!--in: 12 7--> placed just before the code block ("\\n" means Enter), and the text the
    user types may appear in the shown output, as it does in a terminal;
  * output that uses tabs must match when the tabs are expanded to the usual 8-column tab stops;
  * <!--exact--> asks for a character-by-character match;
  * <!--skip--> marks programs that are broken on purpose or print something different on every run:
    they are compiled (to see the error) but not compared;
  * "Predict the output" fragments in the lessons are wrapped in a main() and compared with the answer in the
    solutions file.

Needs GCC: on the PATH, or in a standard Code::Blocks / MSYS2 installation. Exit status 1 if anything fails.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"^(\s*)```(\w*)\s*$")
EXLINE = re.compile(r"^\s*(?:[-*]\s+)?\*\*Ex (\d+)\.(\d+)")
MARK = re.compile(r"^\s*<!--(in:(.*)|skip|exact)-->\s*$")
HEADERS = "".join(f"#include <{h}.h>\n" for h in ("stdio", "string", "ctype", "stdlib", "math", "limits"))


def find_gcc():
    gcc = shutil.which("gcc")
    if gcc:
        return gcc
    for c in (r"C:\Program Files\CodeBlocks\MinGW\bin\gcc.exe", r"C:\Program Files (x86)\CodeBlocks\MinGW\bin\gcc.exe",
              r"C:\msys64\ucrt64\bin\gcc.exe", r"C:\msys64\mingw64\bin\gcc.exe"):
        if Path(c).exists():
            return c
    sys.exit("GCC was not found. Install it (see README section 4) or add it to your PATH.")


def parse(path):
    """Return the code blocks of a Markdown file with their exercise number, section and test marker."""
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks, ex, part, marker, i = [], None, None, None, 0
    while i < len(lines):
        line = lines[i]
        m = EXLINE.match(line)
        if m:
            ex = f"{m.group(1)}.{m.group(2)}"
        if line.startswith("## "):
            part = line[3:]
        mk = MARK.match(line)
        if mk:
            marker = ("in", mk.group(2).strip()) if mk.group(2) is not None else (mk.group(1), None)
            i += 1
            continue
        f = FENCE.match(line)
        if f:
            indent, lang, j, body = f.group(1), f.group(2), i + 1, []
            while j < len(lines) and not re.match(r"^\s*```\s*$", lines[j]):
                body.append(lines[j][len(indent):] if lines[j].startswith(indent) else lines[j].lstrip())
                j += 1
            blocks.append(dict(lang=lang, code="\n".join(body), line=i + 1, end=j + 1, ex=ex, part=part or "", marker=marker))
            marker, i = None, j + 1
            continue
        i += 1
    return blocks


def answers(path):
    """Exercise number -> the answer given in a solutions file (an output block, or the first `code` on its line)."""
    text = path.read_text(encoding="utf-8")
    starts = [(m.start(), f"{m.group(1)}.{m.group(2)}")
              for m in re.finditer(r"^[ \t]*(?:[-*][ \t]+)?\*\*Ex (\d+)\.(\d+)[^*\n]*\*\*", text, re.M)]
    res = {}
    for k, (pos, ex) in enumerate(starts):
        seg = text[pos: starts[k + 1][0] if k + 1 < len(starts) else len(text)]
        block = re.search(r"```output\n(.*?)\n\s*```", seg, re.S)
        inline = re.findall(r"`([^`]+)`", seg.split("\n", 1)[0])
        res[ex] = block.group(1) if block else (inline[0] if inline else None)
    return res


def run(gcc, workdir, name, code, stdin_text):
    src, exe = workdir / f"{name}.c", workdir / f"{name}.exe"
    src.write_text(code + "\n", encoding="utf-8")
    env = dict(os.environ, PATH=str(Path(gcc).parent) + os.pathsep + os.environ.get("PATH", ""))
    cp = subprocess.run([gcc, "-Wall", "-Wextra", "-o", str(exe), str(src), "-lm"], capture_output=True, text=True, env=env)
    if cp.returncode != 0:
        return dict(compiled=False, msg=cp.stderr)
    data = (stdin_text.replace("\\n", "\n") + "\n") if stdin_text is not None else ""
    try:
        r = subprocess.run([str(exe)], input=data.encode(), capture_output=True, timeout=10, env=env)
        out = r.stdout.decode("utf-8", "replace").replace("\r\n", "\n")
    except subprocess.TimeoutExpired:
        out = "<<the program did not finish within 10 seconds>>"
    return dict(compiled=True, out=out, warnings=cp.stderr)


def lines_of(s):
    return [x.rstrip() for x in s.rstrip().split("\n")]


def typed_input_fits(actual, shown, typed):
    """Is `shown` the same as `actual` with the typed input inserted (in order) somewhere? Whitespace is ignored."""
    a, e = "".join(actual.split()), "".join(shown.split())
    toks = typed.replace("\\n", " ").split()
    total = [0]
    for t in toks:
        total.append(total[-1] + len(t))
    if len(e) != len(a) + total[-1]:
        return False
    seen, stack = set(), [(0, 0)]
    while stack:
        j, k = stack.pop()
        if (j, k) in seen:
            continue
        seen.add((j, k))
        i = j + total[k]
        if j == len(a) and k == len(toks):
            return True
        if k < len(toks) and e.startswith(toks[k], i):
            stack.append((j, k + 1))
        if j < len(a) and i < len(e) and e[i] == a[j]:
            stack.append((j + 1, k))
    return False


def compare(actual, shown, marker):
    kind, typed = marker or (None, None)
    if lines_of(actual) == lines_of(shown):
        return None
    if kind == "exact":
        return "the output differs (character by character)"
    if "\t" in actual and "\t" not in shown:
        if [x.expandtabs(8) for x in lines_of(actual)] == lines_of(shown):
            return None
        if actual.split() == shown.split():
            return "the tabs do not line up as shown (real tab stops are every 8 columns)"
    if actual.split() == shown.split():
        return None                                  # only spacing differs, e.g. tabs shown as spaces
    if typed is not None and typed_input_fits(actual, shown, typed):
        return None
    return "the output differs"


def main():
    gcc = find_gcc()
    patterns = sys.argv[1:] or ["lessons/*.md", "solutions/*.md", "appendix/*.md"]
    files = [p for pat in patterns for p in sorted(ROOT.glob(pat))]
    jobs = []                       # (label, code, input, expected, marker, kind)
    for path in files:
        blocks = parse(path)
        sol = answers(ROOT / "solutions" / path.name) if path.parent.name == "lessons" and (ROOT / "solutions" / path.name).exists() else {}
        for k, b in enumerate(blocks):
            if b["lang"] != "c":
                continue
            label = f"{path.relative_to(ROOT).as_posix()}:{b['line']}" + (f" (Ex {b['ex']})" if b["ex"] else "")
            marker = b["marker"]
            typed = marker[1] if marker and marker[0] == "in" else None
            if re.search(r"\bmain\s*\(", b["code"]):
                nxt = blocks[k + 1] if k + 1 < len(blocks) else None
                shown = nxt["code"] if nxt and nxt["lang"] == "output" and nxt["line"] - b["end"] <= 4 else None
                if shown is None and "Predict" in b["part"]:
                    shown = sol.get(b["ex"])
                jobs.append((label, b["code"], typed, shown, marker, "program"))
            elif "Predict" in b["part"] and sol.get(b["ex"]) is not None:
                if typed is None and re.search(r"\b(scanf|getchar|fgets)\s*\(", b["code"]):
                    continue                                 # the input is described in words; check by hand
                jobs.append((label, HEADERS + "int main(void)\n{\n" + b["code"] + "\nreturn 0;\n}", typed, sol[b["ex"]], marker, "fragment"))

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
            results = list(pool.map(lambda nj: run(gcc, work, f"p{nj[0]}", nj[1][1], nj[1][2]), enumerate(jobs)))

    problems, counts = [], dict(compared=0, broken_on_purpose=0, no_output_shown=0, fragments=0)
    for (label, _code, _typed, shown, marker, kind), res in zip(jobs, results):
        skip = marker is not None and marker[0] == "skip"
        if not res["compiled"]:
            if skip:
                counts["broken_on_purpose"] += 1
            else:
                first = next((x for x in res["msg"].splitlines() if "error" in x), res["msg"].strip()[:200])
                problems.append((label, "does not compile: " + first.split(".c:", 1)[-1].strip()))
            continue
        if skip:
            counts["broken_on_purpose"] += 1
            continue
        if shown is None:
            counts["no_output_shown"] += 1
            continue
        why = compare(res["out"], shown, marker)
        counts["fragments" if kind == "fragment" else "compared"] += 1
        if why:
            problems.append((label, f"{why}\n      shown : {shown.strip()[:160]!r}\n      actual: {res['out'].strip()[:160]!r}"))

    print(f"GCC: {gcc}")
    print(f"{counts['compared']} programs and {counts['fragments']} 'predict the output' fragments compared with the text; "
          f"{counts['broken_on_purpose']} programs marked as broken on purpose; {counts['no_output_shown']} programs show no output.")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for label, why in problems:
            print(f"  {label}: {why}")
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
