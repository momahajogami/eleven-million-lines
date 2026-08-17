#!/usr/bin/env python3
"""Generate PDFs for Unit 02 practice — problem sets and reading exercises."""

import re
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

DARK   = colors.HexColor("#1a1a1a")
MID    = colors.HexColor("#444444")
LIGHT  = colors.HexColor("#888888")
RULE   = colors.HexColor("#cccccc")
ACCENT = colors.HexColor("#8b3a3a")
TEAL   = colors.HexColor("#2a5a5a")   # reading exercises use teal

def make_styles(accent=ACCENT):
    return {
        "title": ParagraphStyle(
            "title", fontName="Times-Bold", fontSize=22, leading=28,
            textColor=DARK, spaceAfter=4, alignment=TA_LEFT),
        "subtitle": ParagraphStyle(
            "subtitle", fontName="Times-Italic", fontSize=12, leading=16,
            textColor=MID, spaceAfter=16, alignment=TA_LEFT),
        "h2": ParagraphStyle(
            "h2", fontName="Helvetica-Bold", fontSize=12, leading=16,
            textColor=accent, spaceBefore=16, spaceAfter=4, alignment=TA_LEFT),
        "h3": ParagraphStyle(
            "h3", fontName="Helvetica-Bold", fontSize=11, leading=14,
            textColor=DARK, spaceBefore=10, spaceAfter=3, alignment=TA_LEFT),
        "body": ParagraphStyle(
            "body", fontName="Times-Roman", fontSize=11, leading=16,
            textColor=DARK, spaceBefore=0, spaceAfter=7, alignment=TA_JUSTIFY),
        "bullet": ParagraphStyle(
            "bullet", fontName="Times-Roman", fontSize=11, leading=15,
            textColor=DARK, spaceBefore=2, spaceAfter=2,
            leftIndent=20, alignment=TA_JUSTIFY),
        "code_block": ParagraphStyle(
            "code_block", fontName="Courier", fontSize=9, leading=13,
            textColor=DARK, spaceBefore=6, spaceAfter=6,
            leftIndent=24, rightIndent=24,
            backColor=colors.HexColor("#f4f4f4")),
        "field": ParagraphStyle(
            "field", fontName="Times-Roman", fontSize=10, leading=14,
            textColor=MID, spaceBefore=1, spaceAfter=1, leftIndent=20),
        "number": ParagraphStyle(
            "number", fontName="Helvetica-Bold", fontSize=11, leading=14,
            textColor=accent, spaceBefore=14, spaceAfter=3),
    }


def inline(text):
    text = text.replace("&", "&amp;")
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier" size="9">\1</font>', text)
    return text


def on_page(canvas, doc, header_left, header_right):
    canvas.saveState()
    w, h = letter
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(inch, h - 0.65*inch, w - inch, h - 0.65*inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(LIGHT)
    canvas.drawString(inch, h - 0.52*inch, header_left)
    canvas.drawRightString(w - inch, h - 0.52*inch, header_right)
    canvas.line(inch, 0.65*inch, w - inch, 0.65*inch)
    canvas.drawCentredString(w / 2, 0.45*inch, str(doc.page))
    canvas.restoreState()


def parse_md(path, styles):
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
            text = (text.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;")
                        .replace("\n", "<br/>")
                        .replace(" ", "&nbsp;"))
            flowables.append(Paragraph(text, styles["code_block"]))
            flowables.append(Spacer(1, 4))
            code_lines.clear()

    while i < len(lines):
        line = lines[i].rstrip("\n")

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

        if not stripped:
            flowables.append(Spacer(1, 5))
            i += 1
            continue

        if stripped in ("---", "***", "___"):
            flowables.append(Spacer(1, 6))
            flowables.append(HRFlowable(width="100%", thickness=0.5,
                                        color=RULE, spaceAfter=6))
            i += 1
            continue

        if stripped.startswith("### "):
            flowables.append(Paragraph(inline(stripped[4:]), styles["h3"]))
            i += 1
            continue

        if stripped.startswith("## "):
            # Check for "## Problem N" or "## Step N" patterns — use number style
            m = re.match(r"## (Problem|Step|Reading Exercise)\s+\d+", stripped)
            text = inline(stripped[3:])
            st = styles["number"] if m else styles["h2"]
            flowables.append(Paragraph(text, st))
            i += 1
            continue

        if stripped.startswith("# "):
            flowables.append(Paragraph(inline(stripped[2:]), styles["title"]))
            i += 1
            if i < len(lines):
                nxt = lines[i].strip()
                if nxt.startswith("*") and nxt.endswith("*") and not nxt.startswith("**"):
                    flowables.append(Paragraph(nxt[1:-1], styles["subtitle"]))
                    i += 1
            continue

        if stripped.startswith("**") and ":**" in stripped:
            flowables.append(Paragraph(inline(stripped), styles["field"]))
            i += 1
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            flowables.append(Paragraph(f"• {inline(stripped[2:])}", styles["bullet"]))
            i += 1
            continue

        m = re.match(r"^\d+\.\s+(.*)", stripped)
        if m:
            flowables.append(Paragraph(inline(m.group(1)), styles["bullet"]))
            i += 1
            continue

        # paragraph
        para_lines = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", "-", "*", "```", "---")):
                break
            para_lines.append(nxt)
            i += 1
        flowables.append(Paragraph(inline(" ".join(para_lines)), styles["body"]))

    return flowables


def build_pdf(md_path, pdf_path, header_left, header_right, accent=ACCENT):
    styles = make_styles(accent)

    doc = SimpleDocTemplate(
        pdf_path, pagesize=letter,
        leftMargin=inch, rightMargin=inch,
        topMargin=1.1*inch, bottomMargin=0.9*inch,
        title=header_left,
        author="Eleven Million Lines You Should Know",
    )

    def first_page(canvas, doc):
        on_page(canvas, doc, header_left, header_right)

    content = parse_md(md_path, styles)
    doc.build(content, onFirstPage=first_page, onLaterPages=first_page)
    print(f"  wrote {os.path.basename(pdf_path)}")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    right = "Unit 02 — Practice"

    problem_sets = [
        ("ps-01-intro.md",    "ps-01-intro.pdf",    "Problem Set 01 — Starting Up",          ACCENT),
        ("ps-02-ontogeny.md", "ps-02-ontogeny.pdf", "Problem Set 02 — Inside the Lineage",   ACCENT),
        ("ps-03-phylogeny.md","ps-03-phylogeny.pdf","Problem Set 03 — The Long Line",         ACCENT),
    ]

    reading_exercises = [
        ("re-01-first-walk.md","re-01-first-walk.pdf","RE 01 — The First Walk",     TEAL),
        ("re-02-main.md",      "re-02-main.pdf",      "RE 02 — Finding main()",     TEAL),
        ("re-03-token.md",     "re-03-token.pdf",     "RE 03 — Following a Token",  TEAL),
        ("re-04-comments.md",  "re-04-comments.pdf",  "RE 04 — The Comment Hunt",   TEAL),
        ("re-05-gcc.md",       "re-05-gcc.pdf",       "RE 05 — GCC from a Distance",TEAL),
    ]

    print("Problem sets…")
    for md, pdf, title, accent in problem_sets:
        build_pdf(os.path.join(here, md), os.path.join(here, pdf), title, right, accent)

    print("Reading exercises…")
    for md, pdf, title, accent in reading_exercises:
        build_pdf(os.path.join(here, md), os.path.join(here, pdf), title, right, accent)

    print("Done. 8 PDFs total.")
