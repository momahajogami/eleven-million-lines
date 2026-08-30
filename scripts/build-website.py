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

  Body paragraphs: the description (one or more paragraphs).

  ## Materials

  - **Name** — description
  - **Name** (`path/`) — description

The script updates docs/NN/index.html from this file.
Unit pages that have no WEBSITE.md are left unchanged.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
INDEX_HTML = ROOT / "docs" / "index.html"
CONTENT_DIR = ROOT / "docs"
UNITS = [f"{n:02d}" for n in range(1, 12)]


# ---------------------------------------------------------------------------
# Shared markdown → HTML helpers
# ---------------------------------------------------------------------------

def inline(text: str) -> str:
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def md_to_html(text: str) -> str:
    """Convert a subset of markdown to HTML (no external deps)."""
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


def inject(html: str, begin_marker: str, end_marker: str, new_content: str) -> str:
    """Replace content between begin/end markers."""
    pattern = re.compile(
        rf"({re.escape(begin_marker)}\n).*?(\n\s*{re.escape(end_marker)})",
        re.DOTALL,
    )
    if not pattern.search(html):
        return None  # markers not found
    return pattern.sub(rf"\g<1>{new_content}\g<2>", html)


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
            print(f"  index: SKIP {section} (no {md_file.name})")
            continue
        new_content = md_to_html(md_file.read_text())
        updated = inject(html, f"<!-- BEGIN:{section} -->", f"<!-- END:{section} -->", new_content)
        if updated is None:
            print(f"  index: WARNING markers for '{section}' not found", file=sys.stderr)
            continue
        if updated != html:
            html = updated
            changed = True
            print(f"  index: updated {section}")
        else:
            print(f"  index: unchanged {section}")
    if changed:
        INDEX_HTML.write_text(html)


# ---------------------------------------------------------------------------
# Unit pages
# ---------------------------------------------------------------------------

def parse_website_md(path: Path) -> dict:
    """
    Parse a WEBSITE.md file into tagline, description HTML, and materials HTML.

    Format:
        First non-blank line → tagline
        Paragraphs until ## Materials → description
        List items after ## Materials → materials
    """
    text = path.read_text()
    lines = text.splitlines()

    # strip leading blanks
    while lines and not lines[0].strip():
        lines.pop(0)

    if not lines:
        return None

    tagline = inline(lines[0].strip())
    rest = lines[1:]

    # split on ## Materials
    materials_lines = []
    desc_lines = []
    in_materials = False
    for line in rest:
        if re.match(r'^##\s+Materials', line):
            in_materials = True
            continue
        if in_materials:
            materials_lines.append(line)
        else:
            desc_lines.append(line)

    description_html = md_to_html("\n".join(desc_lines)) if desc_lines else ""
    materials_html = md_to_html("\n".join(materials_lines)) if materials_lines else \
        '    <p class="coming-soon">Coming soon.</p>'

    return {
        "tagline": tagline,
        "description": description_html,
        "materials": materials_html,
    }


def build_unit_page(unit: str) -> bool:
    website_md = ROOT / unit / "WEBSITE.md"
    unit_html = ROOT / "docs" / unit / "index.html"

    if not website_md.exists():
        return False
    if not unit_html.exists():
        print(f"  unit {unit}: WARNING no HTML page at {unit_html}", file=sys.stderr)
        return False

    parsed = parse_website_md(website_md)
    if not parsed:
        return False

    html = unit_html.read_text()
    original = html

    # tagline
    html = re.sub(
        r'(<p class="tagline">).*?(</p>)',
        rf'\g<1>{parsed["tagline"]}\g<2>',
        html,
        flags=re.DOTALL,
    )

    # description div — replace everything inside
    html = re.sub(
        r'(<div class="description">)\s*.*?\s*(</div>)',
        rf'\g<1>\n{parsed["description"]}\n  \g<2>',
        html,
        flags=re.DOTALL,
    )

    # materials div — replace content after <h2>Materials</h2>
    html = re.sub(
        r'(<div class="materials">\s*<h2>Materials</h2>)\s*.*?\s*(</div>)',
        rf'\g<1>\n{parsed["materials"]}\n  \g<2>',
        html,
        flags=re.DOTALL,
    )

    if html != original:
        unit_html.write_text(html)
        print(f"  unit {unit}: updated ← {unit}/WEBSITE.md")
        return True
    else:
        print(f"  unit {unit}: unchanged")
        return False


def build_units():
    any_changed = False
    for unit in UNITS:
        changed = build_unit_page(unit)
        if changed:
            any_changed = True
    return any_changed


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
