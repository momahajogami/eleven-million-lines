#!/usr/bin/env python3
"""
Build the course website from markdown source files.

Usage: python3 scripts/build-website.py

--- Index page ---
Sections in docs/index.html are marked with HTML comment pairs:
  <!-- BEGIN:sectionname -->
  <!-- END:sectionname -->
Each section is sourced from docs/<sectionname>.md

--- Unit pages ---
Each unit directory (01/ through 11/) may contain a WEBSITE.md file.
Format:

  First line: the tagline (short, shown in italic under the title)

  Body paragraphs: the description.

  ## Materials

  - **Name.md** — description    ← .md files get a "read →" link + generated essay page
  - **Name** (`path/`) — description

  ## Repos

  - [Name](https://github.com/...) — description

--- Essay pages ---
For every .md file named in ## Materials, the script:
  1. Reads NN/NAME.md
  2. Converts it to full HTML with course typography
  3. Writes docs/NN/name.html (lowercased)
  4. Adds prev/next navigation based on Materials order
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
INDEX_HTML = ROOT / "docs" / "index.html"
CONTENT_DIR = ROOT / "docs"
UNITS = [f"{n:02d}" for n in range(1, 12)]


# ---------------------------------------------------------------------------
# Inline markdown → HTML
# ---------------------------------------------------------------------------

def inline(text: str) -> str:
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


# ---------------------------------------------------------------------------
# Full markdown → HTML (for essay pages)
# ---------------------------------------------------------------------------

def essay_md_to_html(text: str) -> str:
    """Convert markdown to HTML suitable for a full essay page."""
    lines = text.splitlines()
    html = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # fenced code block
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # consume closing ```
            code = "\n".join(code_lines)
            # escape HTML entities in code
            code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            html.append(f'<pre><code>{code}</code></pre>')
            continue

        # horizontal rule
        if re.match(r'^---+\s*$', line) or re.match(r'^\*\*\*+\s*$', line):
            html.append('<hr>')
            i += 1
            continue

        # headings
        m = re.match(r'^(#{1,3})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            content = inline(m.group(2))
            html.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # blockquote
        if line.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].startswith("> "):
                quote_lines.append(inline(lines[i][2:]))
                i += 1
            html.append("<blockquote>\n  <p>" + "<br>\n  ".join(quote_lines) + "</p>\n</blockquote>")
            continue

        # unordered list
        if re.match(r'^- ', line):
            items = []
            while i < len(lines) and re.match(r'^- ', lines[i]):
                items.append(f"  <li>{inline(lines[i][2:].strip())}</li>")
                i += 1
            html.append("<ul>\n" + "\n".join(items) + "\n</ul>")
            continue

        # ordered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                content = re.sub(r'^\d+\. ', '', lines[i])
                items.append(f"  <li>{inline(content.strip())}</li>")
                i += 1
            html.append("<ol>\n" + "\n".join(items) + "\n</ol>")
            continue

        # blank line
        if not line.strip():
            i += 1
            continue

        # table
        if "|" in line and i + 1 < len(lines) and re.match(r'^[\s|:-]+$', lines[i + 1]):
            headers = [inline(c.strip()) for c in line.strip().strip("|").split("|")]
            i += 2  # skip separator row
            rows = []
            while i < len(lines) and "|" in lines[i]:
                cells = [inline(c.strip()) for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            th = "".join(f"<th>{h}</th>" for h in headers)
            trs = "".join(
                "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
                for row in rows
            )
            html.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue

        # paragraph — collect until blank line or block-level element
        para_lines = []
        while i < len(lines) and lines[i].strip() and \
              not lines[i].startswith("#") and \
              not lines[i].startswith("- ") and \
              not lines[i].startswith("> ") and \
              not lines[i].strip().startswith("```") and \
              not re.match(r'^---+\s*$', lines[i]) and \
              not re.match(r'^\d+\. ', lines[i]):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            html.append(f"<p>{inline(' '.join(para_lines))}</p>")
        else:
            i += 1  # safety: always advance to prevent infinite loop
        continue

    return "\n".join(html)


def extract_title(md_text: str) -> str:
    """Pull the first # heading from markdown as the page title."""
    for line in md_text.splitlines():
        m = re.match(r'^#\s+(.*)', line)
        if m:
            return m.group(1).strip()
    return ""


# ---------------------------------------------------------------------------
# Simple markdown → HTML (for unit page fragments)
# ---------------------------------------------------------------------------

def md_to_html(text: str) -> str:
    lines = text.strip().splitlines()
    html_parts = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(inline(lines[i][2:].strip()))
                i += 1
            html_parts.append(
                "    <ul>\n"
                + "".join(f"      <li>{item}</li>\n" for item in items)
                + "    </ul>"
            )
            continue
        para_lines = []
        while i < len(lines) and lines[i].strip():
            para_lines.append(lines[i].strip())
            i += 1
        html_parts.append("    <p>\n      " + inline(" ".join(para_lines)) + "\n    </p>")
    return "\n".join(html_parts)


def repos_to_html(text: str) -> str:
    lines = text.strip().splitlines()
    items = [inline(l[2:].strip()) for l in lines if l.startswith("- ")]
    if not items:
        return '    <p class="coming-soon">Coming soon.</p>'
    return (
        "    <ul>\n"
        + "".join(f"      <li>{item}</li>\n" for item in items)
        + "    </ul>"
    )


def inject(html: str, begin_marker: str, end_marker: str, new_content: str):
    pattern = re.compile(
        rf"({re.escape(begin_marker)}\n).*?(\n\s*{re.escape(end_marker)})",
        re.DOTALL,
    )
    if not pattern.search(html):
        return None
    return pattern.sub(rf"\g<1>{new_content}\g<2>", html)


# ---------------------------------------------------------------------------
# Essay page HTML template
# ---------------------------------------------------------------------------

ESSAY_CSS = """
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: 18px; }
    body {
      font-family: Georgia, "Times New Roman", serif;
      background: #fdfaf5;
      color: #1a1a1a;
      line-height: 1.75;
      max-width: 720px;
      margin: 0 auto;
      padding: 4rem 2rem 6rem;
    }
    .nav {
      font-size: 0.85rem;
      color: #888;
      margin-bottom: 3rem;
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
    }
    .nav a { color: #555; text-decoration: none; }
    .nav a:hover { text-decoration: underline; }
    .nav .sep { color: #ccc; }
    h1 { font-size: 1.9rem; font-weight: normal; line-height: 1.2; margin-bottom: 2rem; }
    h2 { font-size: 1.15rem; font-weight: bold; margin: 2.5rem 0 0.75rem; }
    h3 { font-size: 1rem; font-weight: bold; font-style: italic; margin: 2rem 0 0.5rem; color: #444; }
    p { margin-bottom: 1.25rem; color: #333; }
    ul, ol { margin: 0 0 1.25rem 1.5rem; color: #333; }
    li { margin-bottom: 0.4rem; }
    code {
      font-family: "Courier New", monospace;
      font-size: 0.85em;
      background: #f0ece4;
      padding: 0.1em 0.35em;
      border-radius: 2px;
    }
    pre {
      background: #f0ece4;
      padding: 1.25rem;
      overflow-x: auto;
      margin-bottom: 1.5rem;
      border-left: 3px solid #c8bfb0;
    }
    pre code { background: none; padding: 0; font-size: 0.82em; }
    blockquote {
      border-left: 3px solid #c8bfb0;
      padding-left: 1.25rem;
      color: #666;
      margin-bottom: 1.25rem;
      font-style: italic;
    }
    hr { border: none; border-top: 1px solid #e0d8cc; margin: 2.5rem 0; }
    strong { color: #1a1a1a; }
    a { color: #555; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 1.5rem; font-size: 0.9rem; }
    th, td { border: 1px solid #e0d8cc; padding: 0.5rem 0.75rem; text-align: left; }
    th { background: #f0ece4; font-weight: bold; }
    .essay-nav {
      margin-top: 4rem;
      padding-top: 1.5rem;
      border-top: 1px solid #e0d8cc;
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
    }
    .essay-nav a { color: #555; text-decoration: none; }
    .essay-nav a:hover { text-decoration: underline; }
    .footer { margin-top: 3rem; font-size: 0.8rem; color: #aaa; border-top: 1px solid #e0d8cc; padding-top: 2rem; }
"""


def render_essay_page(unit: str, unit_title: str, title: str, body_html: str,
                       prev_item: dict | None, next_item: dict | None) -> str:
    page_title = f"{title} — Unit {unit} — Eleven Million Lines" if title else \
                 f"Unit {unit} — Eleven Million Lines"

    prev_html = f'<a href="{prev_item["html"]}">← {prev_item["title"]}</a>' \
                if prev_item else '<span></span>'
    next_html = f'<a href="{next_item["html"]}">{next_item["title"]} →</a>' \
                if next_item else '<span></span>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <style>{ESSAY_CSS}  </style>
</head>
<body>

  <div class="nav">
    <a href="index.html">← Unit {unit}: {unit_title}</a>
  </div>

  <div class="essay">
    {body_html}
  </div>

  <div class="essay-nav">
    {prev_html}
    {next_html}
  </div>

  <div class="footer">Eleven Million Lines You Should Know</div>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Parse WEBSITE.md
# ---------------------------------------------------------------------------

def parse_website_md(path: Path, unit: str) -> dict:
    text = path.read_text()
    lines = text.splitlines()

    while lines and not lines[0].strip():
        lines.pop(0)
    if not lines:
        return None

    tagline = inline(lines[0].strip())
    rest = lines[1:]

    materials_lines, repos_lines, desc_lines = [], [], []
    mode = "desc"

    for line in rest:
        if re.match(r'^##\s+Materials', line):
            mode = "materials"
            continue
        if re.match(r'^##\s+Repos', line):
            mode = "repos"
            continue
        if mode == "materials":
            materials_lines.append(line)
        elif mode == "repos":
            repos_lines.append(line)
        else:
            desc_lines.append(line)

    # extract ordered list of .md essay files from Materials
    # supports optional path hint: **NAME.md** (`subdir/`) — description
    essays = []  # [{"md": "NAME.md", "path": "subdir/NAME.md", "html": "name.html", "title": ""}]
    for line in materials_lines:
        m = re.match(r'^-\s+\*\*([^*]+\.md)\*\*(?:\s+\(`([^`]+)`\))?', line)
        if m:
            md_name = m.group(1)
            path_hint = m.group(2) or ""  # e.g. "scratch/" or ""
            path_hint = path_hint.rstrip("/")
            rel_path = f"{path_hint}/{md_name}" if path_hint else md_name
            html_name = md_name.lower().replace(".md", ".html")
            essays.append({"md": md_name, "path": rel_path, "html": html_name, "title": ""})

    # build materials HTML with links to generated essay pages
    def mat_to_html(lines, unit, essays):
        essay_map = {e["md"]: e for e in essays}  # keyed by filename only
        html_parts = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            if line.startswith("- "):
                items = []
                while i < len(lines) and lines[i].startswith("- "):
                    raw = lines[i][2:].strip()
                    item_html = inline(raw)
                    md_match = re.match(r'\*\*([^*]+\.md)\*\*', raw)
                    if md_match:
                        md_name = md_match.group(1)
                        if md_name in essay_map:
                            href = essay_map[md_name]["html"]
                            item_html += f' <a href="{href}" class="read-link">read →</a>'
                    items.append(item_html)
                    i += 1
                html_parts.append(
                    "    <ul>\n"
                    + "".join(f"      <li>{item}</li>\n" for item in items)
                    + "    </ul>"
                )
                continue
            para_lines = []
            while i < len(lines) and lines[i].strip():
                para_lines.append(lines[i].strip())
                i += 1
            html_parts.append("    <p>\n      " + inline(" ".join(para_lines)) + "\n    </p>")
        return "\n".join(html_parts)

    materials_html = mat_to_html(materials_lines, unit, essays) if materials_lines else \
        '    <p class="coming-soon">Coming soon.</p>'
    repos_html = repos_to_html("\n".join(repos_lines)) if repos_lines else \
        '    <p class="coming-soon">Coming soon.</p>'
    description_html = md_to_html("\n".join(desc_lines)) if desc_lines else ""

    return {
        "tagline": tagline,
        "description": description_html,
        "materials": materials_html,
        "repos": repos_html,
        "essays": essays,
    }


# ---------------------------------------------------------------------------
# Index page
# ---------------------------------------------------------------------------

def build_index():
    html = INDEX_HTML.read_text()
    changed = False
    for match in re.finditer(r"<!-- BEGIN:(\w+) -->", html):
        section = match.group(1)
        md_file = CONTENT_DIR / f"{section}.md"
        if not md_file.exists():
            continue
        new_content = md_to_html(md_file.read_text())
        updated = inject(html, f"<!-- BEGIN:{section} -->", f"<!-- END:{section} -->", new_content)
        if updated is None:
            continue
        if updated != html:
            html = updated
            changed = True
            print(f"  index: updated {section}")
    if changed:
        INDEX_HTML.write_text(html)


# ---------------------------------------------------------------------------
# Unit + essay pages
# ---------------------------------------------------------------------------

def get_unit_title(unit: str) -> str:
    p = ROOT / "docs" / unit / "index.html"
    if not p.exists():
        return unit
    m = re.search(r'<h1>([^<]+)</h1>', p.read_text())
    return m.group(1).strip() if m else unit


def discover_md_files(unit: str) -> list:
    """
    Find all .md files in the unit directory, recursively, skipping git repos.
    Returns list of {"src": Path, "html": "slug.html", "label": "rel/path.md"}.
    Excludes WEBSITE.md and README.md.
    """
    unit_dir = ROOT / unit
    exclude_names = {"WEBSITE.md", "README.md"}
    found = []
    seen_srcs = set()
    seen_htmls = set()

    def walk(directory: Path):
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                if (item / ".git").exists():
                    continue
                walk(item)
            elif item.suffix == ".md" and item.name not in exclude_names:
                if item in seen_srcs:
                    continue
                seen_srcs.add(item)
                rel = item.relative_to(unit_dir)
                parts = list(rel.parts)
                html_name = "-".join(parts).lower().replace(".md", ".html")
                base = html_name
                counter = 1
                while html_name in seen_htmls:
                    html_name = f"{base[:-5]}-{counter}.html"
                    counter += 1
                seen_htmls.add(html_name)
                found.append({"src": item, "html": html_name, "label": str(rel)})

    walk(unit_dir)
    return found


def build_unit_page(unit: str) -> bool:
    website_md = ROOT / unit / "WEBSITE.md"
    unit_html = ROOT / "docs" / unit / "index.html"

    if not website_md.exists():
        return False
    if not unit_html.exists():
        print(f"  unit {unit}: WARNING no HTML page", file=sys.stderr)
        return False

    parsed = parse_website_md(website_md, unit)
    if not parsed:
        return False

    # --- update unit index.html ---
    html = unit_html.read_text()
    original = html

    html = re.sub(r'(<p class="tagline">).*?(</p>)',
                  rf'\g<1>{parsed["tagline"]}\g<2>', html, flags=re.DOTALL)
    html = re.sub(r'(<div class="description">)\s*.*?\s*(</div>)',
                  rf'\g<1>\n{parsed["description"]}\n  \g<2>', html, flags=re.DOTALL)
    html = re.sub(r'(<div class="materials">\s*<h2>Materials</h2>)\s*.*?\s*(</div>)',
                  rf'\g<1>\n{parsed["materials"]}\n  \g<2>', html, flags=re.DOTALL)
    html = re.sub(r'(<div class="repos">\s*<h2>Repositories</h2>)\s*.*?\s*(</div>)',
                  rf'\g<1>\n{parsed["repos"]}\n  \g<2>', html, flags=re.DOTALL)

    unit_changed = html != original
    if unit_changed:
        unit_html.write_text(html)
        print(f"  unit {unit}: updated index")

    # --- build essay pages ---
    # First: Materials-listed essays (curated, with prev/next)
    essays = parsed["essays"]
    unit_title = get_unit_title(unit)
    essay_count = 0
    generated_htmls = set()
    generated_srcs = set()  # track by resolved source path to avoid duplicates

    for idx, essay in enumerate(essays):
        md_path = ROOT / unit / essay["path"]
        if not md_path.exists():
            print(f"  unit {unit}: SKIP {essay['md']} (not found at {essay['path']})", flush=True)
            continue

        md_text = md_path.read_text()
        title = extract_title(md_text)
        essay["title"] = title or essay["md"]

        body_html = essay_md_to_html(md_text)
        prev_item = essays[idx - 1] if idx > 0 else None
        next_item = essays[idx + 1] if idx < len(essays) - 1 else None

        if prev_item and not prev_item.get("title"):
            prev_item = dict(prev_item); prev_item["title"] = prev_item["md"]
        if next_item and not next_item.get("title"):
            next_item = dict(next_item); next_item["title"] = next_item["md"]

        page_html = render_essay_page(unit, unit_title, title, body_html, prev_item, next_item)
        out_path = ROOT / "docs" / unit / essay["html"]
        existing = out_path.read_text() if out_path.exists() else ""
        if page_html != existing:
            out_path.write_text(page_html)
            essay_count += 1
            print(f"  unit {unit}: wrote {essay['html']}", flush=True)
        generated_htmls.add(essay["html"])
        generated_srcs.add(md_path.resolve())

    # Second: auto-discover ALL .md files in unit and generate pages for any not yet done
    discovered = discover_md_files(unit)
    for doc in discovered:
        out_path = ROOT / "docs" / unit / doc["html"]
        if doc["src"].resolve() in generated_srcs:
            # same file already generated by Materials pass — reuse that html name
            doc["html"] = next((e["html"] for e in essays
                                if (ROOT / unit / e["path"]).resolve() == doc["src"].resolve()),
                               doc["html"])
            continue
        md_text = doc["src"].read_text()
        title = extract_title(md_text) or doc["label"]
        body_html = essay_md_to_html(md_text)
        page_html = render_essay_page(unit, unit_title, title, body_html, None, None)
        existing = out_path.read_text() if out_path.exists() else ""
        if page_html != existing:
            out_path.write_text(page_html)
            essay_count += 1
            print(f"  unit {unit}: wrote {doc['html']} ({doc['label']})", flush=True)
        generated_htmls.add(doc["html"])

    # Build the documents section HTML (all discovered .md files as links)
    if discovered:
        items = []
        for doc in discovered:
            title = extract_title(doc["src"].read_text()) or doc["label"]
            items.append(f'      <li><a href="{doc["html"]}">{title}</a> <span class="doc-path">{doc["label"]}</span></li>')
        docs_html = "    <ul>\n" + "\n".join(items) + "\n    </ul>"
    else:
        docs_html = '    <p class="coming-soon">No documents yet.</p>'

    # inject documents section into unit index.html
    html2 = unit_html.read_text()
    updated2 = re.sub(
        r'(<div class="documents">\s*<h2>Documents</h2>)\s*.*?\s*(</div>)',
        rf'\g<1>\n{docs_html}\n  \g<2>',
        html2, flags=re.DOTALL,
    )
    if updated2 != html2:
        unit_html.write_text(updated2)
        print(f"  unit {unit}: updated documents section", flush=True)

    if not unit_changed and essay_count == 0 and updated2 == html2:
        print(f"  unit {unit}: unchanged", flush=True)

    return unit_changed or essay_count > 0


def build_units():
    for unit in UNITS:
        build_unit_page(unit)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=== index page ===")
    build_index()
    print("\n=== unit pages ===")
    build_units()
    print("\nDone.")


if __name__ == "__main__":
    main()
