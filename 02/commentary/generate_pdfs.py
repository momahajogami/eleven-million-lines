#!/usr/bin/env python3
"""Generate PDFs from the Unit 02 commentary markdown files."""

import re
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Colour palette ────────────────────────────────────────────────────────────
DARK   = colors.HexColor("#1a1a1a")
MID    = colors.HexColor("#444444")
LIGHT  = colors.HexColor("#888888")
RULE   = colors.HexColor("#cccccc")
ACCENT = colors.HexColor("#8b3a3a")   # deep autumn red — Cleveland fall

# ── Styles ────────────────────────────────────────────────────────────────────
def make_styles():
    return {
        "title": ParagraphStyle(
            "title",
            fontName="Times-Bold",
            fontSize=22,
            leading=28,
            textColor=DARK,
            spaceAfter=6,
            alignment=TA_LEFT,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            fontName="Times-Italic",
            fontSize=12,
            leading=16,
            textColor=MID,
            spaceAfter=18,
            alignment=TA_LEFT,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=ACCENT,
            spaceBefore=18,
            spaceAfter=6,
            alignment=TA_LEFT,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=DARK,
            spaceBefore=12,
            spaceAfter=4,
            alignment=TA_LEFT,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Times-Roman",
            fontSize=11,
            leading=16,
            textColor=DARK,
            spaceBefore=0,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Times-Roman",
            fontSize=11,
            leading=15,
            textColor=DARK,
            spaceBefore=2,
            spaceAfter=2,
            leftIndent=20,
            bulletIndent=6,
            alignment=TA_JUSTIFY,
        ),
        "code_block": ParagraphStyle(
            "code_block",
            fontName="Courier",
            fontSize=9,
            leading=13,
            textColor=DARK,
            spaceBefore=8,
            spaceAfter=8,
            leftIndent=24,
            rightIndent=24,
            backColor=colors.HexColor("#f5f5f5"),
        ),
        "field": ParagraphStyle(
            "field",
            fontName="Times-Roman",
            fontSize=10,
            leading=14,
            textColor=MID,
            spaceBefore=1,
            spaceAfter=1,
            leftIndent=20,
        ),
        "caption": ParagraphStyle(
            "caption",
            fontName="Times-Italic",
            fontSize=10,
            leading=14,
            textColor=LIGHT,
            spaceBefore=4,
            spaceAfter=12,
            alignment=TA_CENTER,
        ),
    }


# ── Inline markup ─────────────────────────────────────────────────────────────
def inline(text, style_name="body"):
    """Convert **bold**, *italic*, and `code` to ReportLab markup."""
    # escape ampersands first (must come before other substitutions)
    text = text.replace("&", "&amp;")
    # bold+italic
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", text)
    # bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # italic (but not the em-dash --)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    # inline code
    text = re.sub(r"`([^`]+)`", r'<font name="Courier" size="9">\1</font>', text)
    return text


# ── Page template with header/footer ─────────────────────────────────────────
def make_page_template(doc, title):
    def on_page(canvas, doc):
        canvas.saveState()
        w, h = letter

        # header rule and title
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(inch, h - 0.65*inch, w - inch, h - 0.65*inch)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(LIGHT)
        canvas.drawString(inch, h - 0.52*inch, title)
        canvas.drawRightString(w - inch, h - 0.52*inch,
                               "Eleven Million Lines You Should Know — Unit 02")

        # footer rule and page number
        canvas.line(inch, 0.65*inch, w - inch, 0.65*inch)
        canvas.drawCentredString(w / 2, 0.45*inch, str(doc.page))
        canvas.restoreState()

    return on_page


# ── Markdown parser ───────────────────────────────────────────────────────────
def parse_md(path, styles):
    """Parse a subset of markdown into a list of Platypus flowables."""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    flowables = []
    i = 0
    in_code = False
    code_lines = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            text = "\n".join(code_lines)
            # escape for reportlab
            text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            text = text.replace("\n", "<br/>").replace(" ", "&nbsp;")
            flowables.append(Paragraph(text, styles["code_block"]))
            flowables.append(Spacer(1, 4))
            code_lines = []

    while i < len(lines):
        line = lines[i].rstrip("\n")

        # fenced code block
        if line.strip().startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        stripped = line.strip()

        # blank line
        if not stripped:
            flowables.append(Spacer(1, 6))
            i += 1
            continue

        # horizontal rule
        if stripped in ("---", "***", "___"):
            flowables.append(Spacer(1, 8))
            flowables.append(HRFlowable(width="100%", thickness=0.5,
                                        color=RULE, spaceAfter=8))
            i += 1
            continue

        # headings
        if stripped.startswith("### "):
            flowables.append(Paragraph(inline(stripped[4:]), styles["h3"]))
            i += 1
            continue

        if stripped.startswith("## "):
            flowables.append(Spacer(1, 4))
            flowables.append(Paragraph(inline(stripped[3:]), styles["h2"]))
            i += 1
            continue

        if stripped.startswith("# "):
            flowables.append(Paragraph(inline(stripped[2:]), styles["title"]))
            i += 1
            # look for italic subtitle on next non-blank line
            if i < len(lines) and lines[i].strip().startswith("*") and \
               lines[i].strip().endswith("*") and not lines[i].strip().startswith("**"):
                sub = lines[i].strip()[1:-1]  # strip surrounding *
                flowables.append(Paragraph(sub, styles["subtitle"]))
                i += 1
            continue

        # definition-style field lines: **Label:** value
        if stripped.startswith("**") and ":**" in stripped:
            flowables.append(Paragraph(inline(stripped), styles["field"]))
            i += 1
            continue

        # bullet list items
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = inline(stripped[2:])
            flowables.append(Paragraph(f"• {text}", styles["bullet"]))
            i += 1
            continue

        # numbered list
        m = re.match(r"^\d+\.\s+(.*)", stripped)
        if m:
            flowables.append(Paragraph(inline(m.group(1)), styles["bullet"]))
            i += 1
            continue

        # regular paragraph (accumulate continuation lines)
        para_lines = [stripped]
        i += 1
        while i < len(lines):
            next_stripped = lines[i].strip()
            if not next_stripped:
                break
            if next_stripped.startswith(("#", "-", "*", "```", "---", "***")):
                break
            para_lines.append(next_stripped)
            i += 1

        text = " ".join(para_lines)
        flowables.append(Paragraph(inline(text), styles["body"]))

    return flowables


# ── Build one PDF ─────────────────────────────────────────────────────────────
def build_pdf(md_path, pdf_path, doc_title):
    styles = make_styles()
    on_page = make_page_template(None, doc_title)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=1.1*inch,
        bottomMargin=0.9*inch,
        title=doc_title,
        author="Eleven Million Lines You Should Know",
    )

    # patch the on_page closure so it has access to doc
    def on_page_final(canvas, doc):
        on_page(canvas, doc)

    content = parse_md(md_path, styles)
    doc.build(content, onFirstPage=on_page_final, onLaterPages=on_page_final)
    print(f"  wrote {pdf_path}")


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))

    docs = [
        ("01-intro.md",    "01-intro.pdf",    "Unit 02 — Introduction"),
        ("02-ontogeny.md", "02-ontogeny.pdf", "Ontogeny: The C Compiler Lineage"),
        ("03-phylogeny.md","03-phylogeny.pdf","Phylogeny: Where Compilers Came From"),
    ]

    print("Generating PDFs…")
    for md_name, pdf_name, title in docs:
        build_pdf(
            os.path.join(here, md_name),
            os.path.join(here, pdf_name),
            title,
        )
    print("Done.")
