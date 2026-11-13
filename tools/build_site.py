#!/usr/bin/env python3
"""
Build the static course website from the Markdown sources.

    python tools/build_site.py          (run from anywhere; paths are relative to this file)

Reads:   README.md, lessons/*.md, solutions/*.md, appendix/*.md
Writes:  docs/            (plain HTML + CSS + JS; served by GitHub Pages)

Requires: markdown-it-py, pygments      (pip install markdown-it-py pygments)
"""
import html
import json
import re
import shutil
from pathlib import Path

from markdown_it import MarkdownIt
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
SITE_TITLE = "The Complete C Programming Course"
REPO_BASE = "/c-programming-course/"          # GitHub Pages project URL prefix (used by 404.html only)
SITE_DESC = ("A complete beginner's C programming course in simple language, with 725 exercises "
             "and full solutions, covering variables, operators, input/output, control flow, "
             "functions, arrays, pointers and strings.")

# ------------------------------------------------------------------ pages
def first_h1(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def build_page_list():
    pages = []
    pages.append(dict(kind="home", src=ROOT / "README.md", out="index.html", title=first_h1(ROOT / "README.md"), ch=None))
    for n in range(10):
        lesson = next((ROOT / "lessons").glob(f"{n:02d}-*.md"))
        sol = next((ROOT / "solutions").glob(f"{n:02d}-*.md"))
        label = re.sub(r"^Chapter \d+\s*[—-]\s*", "", first_h1(lesson))
        pages.append(dict(kind="lesson", src=lesson, out=f"lessons/{lesson.stem}.html", title=first_h1(lesson), ch=n, label=label))
        pages.append(dict(kind="solution", src=sol, out=f"solutions/{sol.stem}.html", title=first_h1(sol), ch=n, label=label))
    for name in ("cheat-sheet", "reference-tables", "errors-and-debugging", "glossary"):
        p = ROOT / "appendix" / f"{name}.md"
        pages.append(dict(kind="appendix", src=p, out=f"appendix/{name}.html", title=first_h1(p), ch=None))
    return pages


# ------------------------------------------------------------------ markdown
MARKER = re.compile(r"^<!--(?:in:.*?|skip|exact)-->[ \t]*\n", re.M)     # invisible test markers
EX_RE = re.compile(r"^\*\*Ex (\d+)\.(\d+)(?:\s*\(([^)]*)\))?\*\*")
CALLOUTS = {"💡": "tip", "⚠️": "warn", "📝": "note", "🔑": "key", "🤔": "tip"}


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s.strip())
    return s.strip("-") or "section"


def plain(inline) -> str:
    out = []
    for c in inline.children or []:
        if c.type in ("text", "code_inline"):
            out.append(c.content)
        elif c.type in ("softbreak", "hardbreak"):
            out.append(" ")
    return "".join(out).strip()


def make_renderer():
    md = MarkdownIt("default", {"html": True})

    def render_fence(self, tokens, idx, options, env):
        tok = tokens[idx]
        info = tok.info.strip().split()[0] if tok.info.strip() else ""
        code = tok.content.rstrip("\n")
        if info == "output":
            return f'<div class="outblock"><div class="outlabel">Output</div><pre><code>{html.escape(code)}</code></pre></div>\n'
        if info:
            try:
                lexer = get_lexer_by_name(info)
                body = highlight(code, lexer, HtmlFormatter(nowrap=True))
                copy = '<button class="copy" type="button" aria-label="Copy code">Copy</button>' if info in ("c", "cpp") else ""
                return f'<div class="code">{copy}<pre class="hl"><code>{body}</code></pre></div>\n'
            except ClassNotFound:
                pass
        return f'<pre class="plain"><code>{html.escape(code)}</code></pre>\n'

    md.add_render_rule("fence", render_fence)
    md.add_render_rule("table_open", lambda self, t, i, o, e: '<div class="table-wrap"><table>\n')
    md.add_render_rule("table_close", lambda self, t, i, o, e: "</table></div>\n")
    return md


def convert(page, md, relroot):
    """Return (html, toc, search_entries) for one page."""
    text = MARKER.sub("", page["src"].read_text(encoding="utf-8"))
    tokens = md.parse(text, {})
    toc, search, used = [], [], set()
    ch_prefix = f'Ch {page["ch"]}' if page["ch"] is not None else ""

    for i, t in enumerate(tokens):
        if t.type == "heading_open":
            inline = tokens[i + 1]
            title = plain(inline)
            slug = slugify(title)
            base, n = slug, 2
            while slug in used:
                slug, n = f"{base}-{n}", n + 1
            used.add(slug)
            t.attrSet("id", slug)
            lvl = int(t.tag[1])
            if lvl in (2, 3):
                toc.append((lvl, title, slug))
            if lvl >= 2:
                search.append([f"{ch_prefix} › {title}".strip(" ›"), f"{page['out']}#{slug}", page["kind"]])
        elif t.type == "paragraph_open":
            inline = tokens[i + 1]
            m = EX_RE.match(inline.content)
            if m:
                eid = f"ex-{m.group(1)}-{m.group(2)}"
                t.attrSet("id", eid)
                rest = inline.content[m.end():].strip()
                rest = re.sub(r"[*`_]", "", rest)[:90]
                label = f"{m.group(3)}: " if m.group(3) else ""
                search.append([f"Ex {m.group(1)}.{m.group(2)} — {label}{rest}".strip(" —"), f"{page['out']}#{eid}", page["kind"]])
        elif t.type == "inline":
            for c in t.children or []:                      # links live inside inline tokens
                if c.type != "link_open":
                    continue
                href = c.attrGet("href") or ""
                if ".md" in href and not href.startswith(("http://", "https://")):
                    path, _, frag = href.partition("#")
                    if path.endswith("README.md"):
                        path = path[: -len("README.md")] + "index.html"
                    elif path.endswith(".md"):
                        path = path[:-3] + ".html"
                    c.attrSet("href", path + (f"#{frag}" if frag else ""))
        elif t.type == "blockquote_open":
            j = i + 1
            while j < len(tokens) and tokens[j].type != "inline":
                j += 1
            first = tokens[j].content.lstrip() if j < len(tokens) else ""
            for emoji, cls in CALLOUTS.items():
                if first.startswith(emoji):
                    t.attrSet("class", f"callout {cls}")
                    break

    return md.renderer.render(tokens, md.options, {}), toc, search


# ------------------------------------------------------------------ templates
def nav_html(pages, current, root):
    chapters = {}
    for p in pages:
        if p["kind"] in ("lesson", "solution"):
            chapters.setdefault(p["ch"], {})[p["kind"]] = p
    parts = ['<div class="nav-section">Start here</div>']
    cls = "nav-link active" if current["kind"] == "home" else "nav-link"
    parts.append(f'<a class="{cls}" href="{root}index.html">Course home</a>')
    parts.append('<div class="nav-section">Chapters</div>')
    for n in sorted(chapters):
        les, sol = chapters[n]["lesson"], chapters[n]["solution"]
        active_row = current.get("ch") == n
        lcls = "nav-ch active" if current is les else "nav-ch"
        scls = "nav-sol active" if current is sol else "nav-sol"
        parts.append(
            f'<div class="nav-row{" on" if active_row else ""}">'
            f'<a class="{lcls}" href="{root}{les["out"]}"><span class="num">{n}</span>{html.escape(les["label"])}</a>'
            f'<a class="{scls}" href="{root}{sol["out"]}" title="Solutions to Chapter {n}">Solutions</a></div>'
        )
    parts.append('<div class="nav-section">Appendix</div>')
    for p in pages:
        if p["kind"] == "appendix":
            c = "nav-link active" if current is p else "nav-link"
            parts.append(f'<a class="{c}" href="{root}{p["out"]}">{html.escape(p["title"])}</a>')
    return "\n".join(parts)


def pager_html(pages, current, root):
    same = [p for p in pages if p["kind"] == current["kind"]]
    if current["kind"] not in ("lesson", "solution"):
        return ""
    k = same.index(current)
    prev = same[k - 1] if k > 0 else None
    nxt = same[k + 1] if k + 1 < len(same) else None
    other_kind = "solution" if current["kind"] == "lesson" else "lesson"
    other = next(p for p in pages if p["kind"] == other_kind and p["ch"] == current["ch"])
    other_txt = (f'Solutions to Chapter {current["ch"]}  →' if current["kind"] == "lesson"
                 else f'←  Back to the Chapter {current["ch"]} lesson')
    out = ['<nav class="pager" aria-label="Page navigation">']
    out.append(f'<a class="pager-main" href="{root}{other["out"]}">{other_txt}</a>')
    out.append('<div class="pager-row">')
    out.append(f'<a class="pager-prev" href="{root}{prev["out"]}"><small>Previous</small>{html.escape(prev["title"])}</a>' if prev else "<span></span>")
    out.append(f'<a class="pager-next" href="{root}{nxt["out"]}"><small>Next</small>{html.escape(nxt["title"])}</a>' if nxt else "<span></span>")
    out.append("</div></nav>")
    return "\n".join(out)


FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230e6b4a'/%3E"
           "%3Ctext x='32' y='44' font-size='34' text-anchor='middle' font-family='Consolas,monospace' "
           "font-weight='700' fill='%23ffd966'%3EC%3C/text%3E%3C/svg%3E")

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="{favicon}">
<script>(function(){{try{{var t=localStorage.getItem('theme');if(!t){{t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}}document.documentElement.setAttribute('data-theme',t)}}catch(e){{document.documentElement.setAttribute('data-theme','light')}}}})()</script>
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body id="top">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <button id="menu" class="icon-btn" aria-label="Open the chapter menu" aria-controls="sidebar" aria-expanded="false">&#9776;</button>
  <a class="brand" href="{root}index.html"><span class="logo">C</span><span class="brand-text">{site}</span></a>
  <div class="search">
    <input id="q" type="search" placeholder="Search topics or jump to an exercise (e.g. Ex 5.67)" autocomplete="off" aria-label="Search the course">
    <div id="results" class="results" hidden></div>
  </div>
  <button id="theme" class="icon-btn" aria-label="Switch between light and dark mode" title="Light / dark">&#9680;</button>
</header>
<div class="layout">
  <nav class="sidebar" id="sidebar" aria-label="Course chapters">
{nav}
  </nav>
  <div class="scrim" id="scrim"></div>
  <main id="main" class="content">
{cta}
    <article>
{body}
    </article>
{pager}
    <footer class="foot">
      <span>{site}</span>
      <a href="#top" class="totop">Back to top &uarr;</a>
    </footer>
  </main>
  <aside class="toc" aria-label="On this page">
{toc}
  </aside>
</div>
<script>window.SITE_ROOT = "{root}";</script>
<script src="{root}assets/app.js" defer></script>
</body>
</html>
"""


def toc_html(toc):
    if len(toc) < 3:
        return ""
    items = []
    for lvl, title, slug in toc:
        items.append(f'<a class="toc-{lvl}" href="#{slug}">{html.escape(title)}</a>')
    return '<div class="toc-title">On this page</div>\n' + "\n".join(items)


# ------------------------------------------------------------------ assets
def pygments_css():
    light = HtmlFormatter(style="friendly").get_style_defs('[data-theme="light"] .hl')
    dark = HtmlFormatter(style="github-dark").get_style_defs('[data-theme="dark"] .hl')
    strip_bg = lambda css: "\n".join(l for l in css.splitlines() if "background" not in l.split("{")[0] and not re.search(r"\.hl\s*\{\s*background", l))
    # keep token colours only; page CSS controls the block background
    def clean(css):
        out = []
        for line in css.splitlines():
            line = re.sub(r"background(-color)?:\s*[^;}]+;?", "", line)
            if re.match(r"^[^{]*\{\s*\}$", line.strip()):
                continue
            out.append(line)
        return "\n".join(out)
    return clean(light) + "\n" + clean(dark)


def main():
    pages = build_page_list()
    md = make_renderer()
    if OUT.exists():
        for child in OUT.iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    asset_dir = Path(__file__).resolve().parent / "site_assets"
    (OUT / "assets" / "style.css").write_text(
        (asset_dir / "style.css").read_text(encoding="utf-8") + "\n/* ---- syntax colours ---- */\n" + pygments_css(),
        encoding="utf-8",
    )
    shutil.copy(asset_dir / "app.js", OUT / "assets" / "app.js")

    index = []
    for page in pages:
        depth = page["out"].count("/")
        root = "../" * depth
        body, toc, search = convert(page, md, root)
        index.extend(search)
        index.append([page["title"], page["out"], page["kind"]])

        cta = ""
        if page["kind"] == "home":
            first = next(p for p in pages if p["kind"] == "lesson")
            cta = (f'<div class="cta"><a class="btn primary" href="{first["out"]}">Start with Chapter 0 &rarr;</a>'
                   f'<a class="btn" href="appendix/cheat-sheet.html">Cheat sheet</a>'
                   f'<a class="btn" href="appendix/errors-and-debugging.html">Debugging guide</a></div>')

        title = page["title"] if page["kind"] == "home" else f'{page["title"]} · {SITE_TITLE}'
        page_html = PAGE.format(
            title=html.escape(title), desc=html.escape(SITE_DESC), favicon=FAVICON, root=root,
            site=html.escape(SITE_TITLE), nav=nav_html(pages, page, root), cta=cta, body=body,
            pager=pager_html(pages, page, root), toc=toc_html(toc),
        )
        target = OUT / page["out"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_html, encoding="utf-8")

    (OUT / "assets" / "search.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    not_found = PAGE.format(
        title=f"Page not found · {SITE_TITLE}", desc=html.escape(SITE_DESC), favicon=FAVICON, root=REPO_BASE,
        site=html.escape(SITE_TITLE), nav=f'<a class="nav-link" href="{REPO_BASE}index.html">Course home</a>', cta="",
        body="<h1>Page not found</h1><p>That page does not exist. <a href=\"./\">Go to the course home page</a>.</p>",
        pager="", toc="",
    )
    (OUT / "404.html").write_text(not_found, encoding="utf-8")
    print(f"built {len(pages)} pages, {len(index)} search entries -> {OUT}")


if __name__ == "__main__":
    main()
