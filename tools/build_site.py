#!/usr/bin/env python3
"""
Build the static course website from the Markdown sources.

    python tools/build_site.py          (run from anywhere; paths are relative to this file)

Reads:   README.md, lessons/*.md, solutions/*.md, appendix/*.md
Writes:  docs/            (plain HTML + CSS + JS; served by GitHub Pages)

Requires: markdown-it-py, pygments      (pip install -r tools/requirements.txt)
"""
import hashlib
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

from markdown_it import MarkdownIt
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
SITE_TITLE = "The Complete C Programming Course"
SITE_SHORT = "COE 281"
REPO_BASE = "/c-programming-course/"          # GitHub Pages project URL prefix (used by 404.html only)
COPYRIGHT_HOLDER = "Mrwhocancreate, founder and CEO, Behemoth Group"
COPYRIGHT_SINCE = 2026                        # first year of publication; later builds show a range, e.g. 2026–2027


def copyright_years() -> str:
    now = date.today().year
    return f"{COPYRIGHT_SINCE}–{now}" if now > COPYRIGHT_SINCE else str(COPYRIGHT_SINCE)

# ------------------------------------------------------------------ pages
def first_h1(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def build_page_list():
    pages = [dict(kind="home", src=ROOT / "README.md", out="index.html", title=first_h1(ROOT / "README.md"), ch=None)]
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

# Callouts: a blockquote whose text starts with one of these emoji becomes a labelled box.
# The emoji itself is removed, so the site stays black and white.
CALLOUTS = {
    "💡": ("tip", "Tip"),
    "🤔": ("tip", "Think"),
    "⚠️": ("warn", "Watch out"),
    "⚠": ("warn", "Watch out"),
    "📝": ("note", "Note"),
    "🔑": ("key", "Key point"),
}
# Colour emoji used as ticks and crosses in tables -> plain monochrome glyphs.
MONO = {"✅": "✓", "❌": "✗", "✔️": "✓", "✔": "✓", "✘": "✗"}

# printf/scanf conversion specifications inside string literals, e.g. %d  %-10s  %8.2f  %lf  %zu  %[^\n]  %%
FMT = re.compile(r"%(?:%|[-+ #0]*(?:\d+|\*)?(?:\.(?:\d+|\*))?(?:hh|h|ll|l|L|z|j|t)?[diouxXfFeEgGaAcspn]|\d*\[[^\]]*\])")


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


def polish_c(body: str) -> str:
    """Small additions to Pygments' C colouring: function calls, and format specifiers inside strings."""
    body = re.sub(r'<span class="n">(\w+)</span>(?=<span class="p">\()', r'<span class="fn">\1</span>', body)
    return re.sub(r'(<span class="s">)(.*?)(</span>)',
                  lambda m: m.group(1) + FMT.sub(lambda f: f'<span class="si">{f.group(0)}</span>', m.group(2)) + m.group(3),
                  body)


def make_renderer():
    md = MarkdownIt("default", {"html": True})

    def render_fence(self, tokens, idx, options, env):
        tok = tokens[idx]
        info = tok.info.strip().split()[0] if tok.info.strip() else ""
        code = tok.content.rstrip("\n")
        if info == "output":
            return (f'<div class="outblock"><div class="outlabel" aria-hidden="true">Output</div>'
                    f'<pre><code>{html.escape(code)}</code></pre></div>\n')
        if info and info != "text":
            try:
                lexer = get_lexer_by_name(info)
                body = highlight(code, lexer, HtmlFormatter(nowrap=True))
                if info == "c":
                    body = polish_c(body)
                label = {"c": "C", "cpp": "C++"}.get(info, info)
                copy = '<button class="copy" type="button" aria-label="Copy code">Copy</button>'
                return (f'<div class="code" data-lang="{html.escape(label)}">{copy}'
                        f'<pre class="hl"><code>{body}</code></pre></div>\n')
            except ClassNotFound:
                pass
        return f'<pre class="plain"><code>{html.escape(code)}</code></pre>\n'

    md.add_render_rule("fence", render_fence)
    md.add_render_rule("table_open", lambda self, t, i, o, e: '<div class="table-wrap"><table>\n')
    md.add_render_rule("table_close", lambda self, t, i, o, e: "</table></div>\n")
    return md


def strip_lead(children, prefix):
    """Remove `prefix` (an emoji) and the spaces after it from the start of an inline token's children."""
    for c in children:
        if c.type == "text":
            if c.content.startswith(prefix):
                c.content = c.content[len(prefix):].lstrip("️").lstrip()
            return


def convert(page, md, text=None):
    """Return (html, toc, search_entries) for one page."""
    text = MARKER.sub("", text if text is not None else page["src"].read_text(encoding="utf-8"))
    for k, v in MONO.items():
        text = text.replace(k, v)
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
                t.attrSet("class", "ex")
                rest = re.sub(r"^Ex \d+\.\d+(\s*\([^)]*\))?\s*", "", plain(inline))[:90]
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
            if j >= len(tokens):
                continue
            first = tokens[j].content.lstrip()
            for emoji, (cls, label) in CALLOUTS.items():
                if first.startswith(emoji):
                    t.attrSet("class", f"callout {cls}")
                    t.attrSet("data-label", label)
                    strip_lead(tokens[j].children or [], emoji)
                    break

    body = md.renderer.render(tokens, md.options, {})
    # hover anchors on section headings
    body = re.sub(r'<h([23]) id="([^"]+)">(.*?)</h\1>',
                  r'<h\1 id="\2">\3<a class="anchor" href="#\2" aria-label="Link to this section">#</a></h\1>', body)
    return body, toc, search


# ------------------------------------------------------------------ icons (inline SVG, inherit the text colour)
def svg(paths, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


ICON_MENU = svg('<path d="M4 6h16M4 12h16M4 18h16"/>')
ICON_SEARCH = svg('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>', "search-icon")
ICON_SUN = svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>', "i-sun")
ICON_MOON = svg('<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>', "i-moon")
ICON_ARROW_L = svg('<path d="M19 12H5M12 19l-7-7 7-7"/>')
ICON_ARROW_R = svg('<path d="M5 12h14M12 5l7 7-7 7"/>')


# ------------------------------------------------------------------ templates
def nav_html(pages, current, root):
    chapters = {}
    for p in pages:
        if p["kind"] in ("lesson", "solution"):
            chapters.setdefault(p["ch"], {})[p["kind"]] = p
    parts = ['<div class="nav-group">',
             f'<a class="nav-link{" active" if current["kind"] == "home" else ""}" href="{root}index.html">Course home</a>',
             '</div>',
             '<div class="nav-title">Chapters</div>',
             '<ol class="nav-chapters">']
    for n in sorted(chapters):
        les, sol = chapters[n]["lesson"], chapters[n]["solution"]
        on = current.get("ch") == n
        parts.append(
            f'<li class="nav-row{" on" if on else ""}">'
            f'<a class="nav-ch{" active" if current is les else ""}" href="{root}{les["out"]}">'
            f'<span class="num">{n:02d}</span><span class="nav-label">{html.escape(les["label"])}</span></a>'
            f'<a class="nav-sol{" active" if current is sol else ""}" href="{root}{sol["out"]}" '
            f'title="Solutions to Chapter {n}" aria-label="Solutions to Chapter {n}">Solutions</a></li>'
        )
    parts.append("</ol>")
    parts.append('<div class="nav-title">Appendix</div><div class="nav-group">')
    for p in pages:
        if p["kind"] == "appendix":
            c = "nav-link active" if current is p else "nav-link"
            parts.append(f'<a class="{c}" href="{root}{p["out"]}">{html.escape(p["title"])}</a>')
    parts.append("</div>")
    return "\n".join(parts)


def pager_html(pages, current, root):
    if current["kind"] not in ("lesson", "solution"):
        return ""
    same = [p for p in pages if p["kind"] == current["kind"]]
    k = same.index(current)
    prev = same[k - 1] if k > 0 else None
    nxt = same[k + 1] if k + 1 < len(same) else None
    other_kind = "solution" if current["kind"] == "lesson" else "lesson"
    other = next(p for p in pages if p["kind"] == other_kind and p["ch"] == current["ch"])
    if current["kind"] == "lesson":
        main_link = (f'<a class="pager-main" href="{root}{other["out"]}"><span>Check your answers</span>'
                     f'<strong>Solutions to Chapter {current["ch"]}</strong>{ICON_ARROW_R}</a>')
    else:
        main_link = (f'<a class="pager-main" href="{root}{other["out"]}"><span>Back to the lesson</span>'
                     f'<strong>Chapter {current["ch"]} — {html.escape(current["label"])}</strong>{ICON_ARROW_L}</a>')
    out = ['<nav class="pager" aria-label="Page navigation">', main_link, '<div class="pager-row">']
    out.append(f'<a class="pager-prev" href="{root}{prev["out"]}"><small>{ICON_ARROW_L} Previous</small>{html.escape(prev["title"])}</a>' if prev else "<span></span>")
    out.append(f'<a class="pager-next" href="{root}{nxt["out"]}"><small>Next {ICON_ARROW_R}</small>{html.escape(nxt["title"])}</a>' if nxt else "<span></span>")
    out.append("</div></nav>")
    return "\n".join(out)


def toc_html(toc):
    if len(toc) < 3:
        return ""
    items = [f'<a class="toc-{lvl}" href="#{slug}">{html.escape(title)}</a>' for lvl, title, slug in toc]
    return '<div class="toc-title">On this page</div>\n<nav class="toc-links">\n' + "\n".join(items) + "\n</nav>"


def eyebrow_html(page):
    if page["kind"] == "lesson":
        return f'<p class="eyebrow">Chapter {page["ch"]} · Lesson</p>'
    if page["kind"] == "solution":
        return f'<p class="eyebrow">Chapter {page["ch"]} · Solutions</p>'
    if page["kind"] == "appendix":
        return '<p class="eyebrow">Appendix</p>'
    return ""


FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230a0a0a'/%3E"
           "%3Ctext x='32' y='45' font-size='36' text-anchor='middle' font-family='Consolas,Menlo,monospace' "
           "font-weight='700' fill='%23ffffff'%3EC%3C/text%3E%3C/svg%3E")

FONTS = ("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700"
         "&family=JetBrains+Mono:ital,wght@0,400;0,600;1,400&display=swap")

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{author}">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script>(function(){{try{{var t=localStorage.getItem('theme');if(!t){{t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}}document.documentElement.setAttribute('data-theme',t)}}catch(e){{document.documentElement.setAttribute('data-theme','light')}}}})()</script>
<link rel="stylesheet" href="{root}assets/style.css?v={ver}">
</head>
<body id="top" class="kind-{kind}">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <button id="menu" class="icon-btn menu-btn" type="button" aria-label="Open the chapter menu" aria-controls="sidebar" aria-expanded="false">{icon_menu}</button>
  <a class="brand" href="{root}index.html" aria-label="{site} — home">
    <span class="logo" aria-hidden="true">C</span>
    <span class="brand-text"><span class="brand-name">{site}</span><span class="brand-sub">{short}</span></span>
  </a>
  <div class="search" role="search">
    {icon_search}
    <input id="q" type="search" placeholder="Search, or jump to Ex 5.67" autocomplete="off" spellcheck="false" aria-label="Search the course">
    <kbd class="search-kbd" aria-hidden="true">/</kbd>
    <div id="results" class="results" hidden></div>
  </div>
  <button id="theme" class="icon-btn" type="button" aria-label="Switch between light and dark mode" title="Light / dark">{icon_sun}{icon_moon}</button>
</header>
<div class="layout">
  <nav class="sidebar" id="sidebar" aria-label="Course chapters">
{nav}
  </nav>
  <div class="scrim" id="scrim"></div>
  <main id="main" class="content">
{hero}
    {eyebrow}
    <article class="prose">
{body}
    </article>
{pager}
    <footer class="foot">
      <div class="foot-text">
        <span class="copyright">&copy; {years} {author}</span>
        <span>{site} · {short}</span>
      </div>
      <a href="#top" class="totop">Back to top</a>
    </footer>
  </main>
  <aside class="toc" aria-label="On this page">
{toc}
  </aside>
</div>
<script>window.SITE_ROOT = "{root}";</script>
<script src="{root}assets/app.js?v={ver}" defer></script>
</body>
</html>
"""


ASSET_VERSION = ""      # set in main(): a short hash of the CSS and JS, so browsers never use stale copies


def render_page(**kw):
    return PAGE.format(ver=ASSET_VERSION, favicon=FAVICON, fonts=FONTS, site=html.escape(SITE_TITLE), short=html.escape(SITE_SHORT),
                       author=html.escape(COPYRIGHT_HOLDER), years=copyright_years(),
                       icon_menu=ICON_MENU, icon_search=ICON_SEARCH, icon_sun=ICON_SUN, icon_moon=ICON_MOON, **kw)


# ------------------------------------------------------------------ home page
def split_readme(md, text):
    """Split README.md into its introduction (shown as the hero) and the rest (shown as the page body)."""
    m = re.search(r"^## ", text, re.M)
    intro, rest = (text[: m.start()], text[m.start():]) if m else ("", text)
    # the "For maintainers" section is for people who edit the course, not for students on the website
    rest = re.sub(r"^## [^\n]*For maintainers.*?(?=^## |\Z)", "", rest, flags=re.M | re.S)
    rest = re.sub(r"(\s*\n---\s*)+\Z", "\n", rest)
    title, sub, lede, audience = SITE_TITLE, "", "", ""
    for block in re.split(r"\n\s*\n", intro):
        b = block.strip()
        if b.startswith("# "):
            title = b[2:].strip()
        elif b.startswith("### "):
            sub = b[4:].strip()
        elif b.startswith(">"):
            audience = re.sub(r"^>\s?", "", b, flags=re.M).strip()
        elif b and not b.startswith(("---", "🌐", "<!--")) and not lede:
            lede = b
    return dict(title=title, sub=sub, lede=md.renderInline(lede), audience=md.renderInline(audience)), rest


def hero_html(info, pages, stats):
    first = next(p for p in pages if p["kind"] == "lesson")
    items = "".join(f'<div class="stat"><dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd></div>' for k, v in stats)
    return f"""    <section class="hero">
      <p class="eyebrow">{html.escape(info["sub"])}</p>
      <h1>{html.escape(info["title"])}</h1>
      <p class="lede">{info["lede"]}</p>
      <p class="audience">{info["audience"]}</p>
      <div class="cta">
        <a class="btn btn-primary" href="{first["out"]}">Start with Chapter 0 {ICON_ARROW_R}</a>
        <a class="btn" href="appendix/cheat-sheet.html">Cheat sheet</a>
        <a class="btn" href="appendix/errors-and-debugging.html">Debugging guide</a>
      </div>
      <dl class="stats">{items}</dl>
    </section>"""


def course_stats():
    exercises = programs = 0
    for f in sorted((ROOT / "lessons").glob("*.md")):
        exercises += len(re.findall(r"^\*\*Ex \d+\.\d+", f.read_text(encoding="utf-8"), re.M))
    for folder in ("lessons", "solutions", "appendix"):
        for f in (ROOT / folder).glob("*.md"):
            for block in re.findall(r"^```c\n(.*?)^```", f.read_text(encoding="utf-8"), re.M | re.S):
                if re.search(r"\bmain\s*\(", block):
                    programs += 1
    return [("Chapters", "10"), ("Exercises", f"{exercises}"), ("Complete programs", f"{programs}"), ("Mock exam", "100 marks")]


# ------------------------------------------------------------------ build
def main():
    pages = build_page_list()
    md = make_renderer()
    if OUT.exists():
        for child in OUT.iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    global ASSET_VERSION
    asset_dir = Path(__file__).resolve().parent / "site_assets"
    shutil.copy(asset_dir / "style.css", OUT / "assets" / "style.css")
    shutil.copy(asset_dir / "app.js", OUT / "assets" / "app.js")
    ASSET_VERSION = hashlib.sha1((asset_dir / "style.css").read_bytes() + (asset_dir / "app.js").read_bytes()).hexdigest()[:10]

    stats = course_stats()
    desc = (f"A complete beginner's course in C programming, in simple language, with {stats[1][1]} exercises "
            "and full solutions: variables, operators, input/output, control flow, functions, arrays, pointers and strings.")

    index = []
    for page in pages:
        root = "../" * page["out"].count("/")
        hero = ""
        if page["kind"] == "home":
            info, rest = split_readme(md, page["src"].read_text(encoding="utf-8"))
            body, toc, search = convert(page, md, rest)
            hero = hero_html(info, pages, stats)
        else:
            body, toc, search = convert(page, md)
        index.extend(search)
        index.append([page["title"], page["out"], page["kind"]])

        title = page["title"] if page["kind"] == "home" else f'{page["title"]} · {SITE_TITLE}'
        page_html = render_page(
            title=html.escape(title), desc=html.escape(desc), root=root, kind=page["kind"],
            nav=nav_html(pages, page, root), hero=hero, eyebrow=eyebrow_html(page), body=body,
            pager=pager_html(pages, page, root), toc=toc_html(toc),
        )
        target = OUT / page["out"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_html, encoding="utf-8")

    (OUT / "assets" / "search.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    not_found = render_page(
        title=f"Page not found · {html.escape(SITE_TITLE)}", desc=html.escape(desc), root=REPO_BASE, kind="notfound",
        nav=f'<div class="nav-group"><a class="nav-link" href="{REPO_BASE}index.html">Course home</a></div>',
        hero="", eyebrow='<p class="eyebrow">Error 404</p>',
        body='<h1>Page not found</h1><p>That page does not exist. Try the search box above, or go to the '
             f'<a href="{REPO_BASE}index.html">course home page</a>.</p>',
        pager="", toc="",
    )
    (OUT / "404.html").write_text(not_found, encoding="utf-8")
    print(f"built {len(pages)} pages, {len(index)} search entries -> {OUT}")


if __name__ == "__main__":
    main()
