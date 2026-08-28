#!/usr/bin/env python3
"""
Build docs/index.html from markdown source files.

Usage: python3 scripts/build-website.py

Sections in index.html are marked with HTML comment pairs:
  <!-- BEGIN:sectionname -->
  <!-- END:sectionname -->

Each section is sourced from docs/<sectionname>.md
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
HTML_FILE = ROOT / "docs" / "index.html"
CONTENT_DIR = ROOT / "docs"


def md_to_html(text: str) -> str:
    """Convert a subset of markdown to HTML (no external deps)."""
    lines = text.strip().splitlines()
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # blank line — skip (paragraph breaks handled below)
        if not line.strip():
            i += 1
            continue

        # unordered list block
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

        # paragraph: gather until blank line
        para_lines = []
        while i < len(lines) and lines[i].strip():
            para_lines.append(lines[i].strip())
            i += 1
        html_parts.append("    <p>\n      " + inline(" ".join(para_lines)) + "\n    </p>")

    return "\n".join(html_parts)


def inline(text: str) -> str:
    """Convert inline markdown (bold, italic, links) to HTML."""
    # links: [text](url)
    text = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'<a href="\2">\1</a>',
        text,
    )
    # bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # italic: *text* (but not **)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text


def inject(html: str, section: str, new_content: str) -> str:
    begin = f"<!-- BEGIN:{section} -->"
    end = f"<!-- END:{section} -->"
    pattern = re.compile(
        rf"({re.escape(begin)}\n).*?(\n\s*{re.escape(end)})",
        re.DOTALL,
    )
    if not pattern.search(html):
        print(f"  WARNING: markers for '{section}' not found in HTML", file=sys.stderr)
        return html
    return pattern.sub(rf"\g<1>{new_content}\g<2>", html)


def main():
    html = HTML_FILE.read_text()
    changed = False

    # find all BEGIN markers and process each
    for match in re.finditer(r"<!-- BEGIN:(\w+) -->", html):
        section = match.group(1)
        md_file = CONTENT_DIR / f"{section}.md"
        if not md_file.exists():
            print(f"  SKIP: {md_file} not found")
            continue
        md = md_file.read_text()
        new_content = md_to_html(md)
        updated = inject(html, section, new_content)
        if updated != html:
            html = updated
            changed = True
            print(f"  updated: {section} ← {md_file.relative_to(ROOT)}")
        else:
            print(f"  unchanged: {section}")

    if changed:
        HTML_FILE.write_text(html)
        print(f"\nWrote {HTML_FILE.relative_to(ROOT)}")
    else:
        print("\nNo changes.")


if __name__ == "__main__":
    main()
