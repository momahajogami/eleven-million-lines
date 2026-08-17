# Commentary — Unit 02: Classic C Compilers

This directory is the annotation layer for Unit 02. The repos it sits beside — `gcc/` and `tcc/` — are primary texts. They are not modified. Everything here lives alongside them, the way a reader's notes live alongside a book.

---

## Structure

```
commentary/
├── README.md                    ← you are here
├── 01-intro.md / .pdf           ← module orientation, repos, reading order, bibliography
├── 02-ontogeny.md / .pdf        ← the C compiler lineage: DMR → PCC → GCC → TCC
├── 03-phylogeny.md / .pdf       ← deeper history: geographies, characters, the long line
└── generate_pdfs.py             ← regenerates the PDFs from the markdown source
```

---

## The three documents

**01-intro** orients the unit. What this module is, what repos are present, what's notable about each, what's not here, reading order, and a bibliography with availability notes.

**02-ontogeny** follows the specific C compiler lineage — the direct developmental line from Ritchie's original through PCC, GCC, and TCC. This is the unit's own evolutionary history: how these specific programs came to exist.

**03-phylogeny** goes deeper: the history of the idea of a compiler, from Turing's theoretical foundations through Grace Hopper's first implementation, Backus's FORTRAN, Bell Labs, Berkeley, MIT. The geographies and characters. The long line.

---

## Format and voice

The markdown files are the source of truth. The PDFs are generated from them — run `python3 generate_pdfs.py` from this directory to regenerate. The script requires `reportlab`.

Voice is the same as Unit 01: opinionated, precise, written to be read. These are not neutral summaries. They say what matters. They say when something is beautiful or strange or important. They are signed by the course.

---

## What these become

Every file here is a course asset: a lecture basis, a discussion prompt, a handout, a reading. The three PDFs can go in front of students immediately. The markdown files continue to grow as the course develops.
