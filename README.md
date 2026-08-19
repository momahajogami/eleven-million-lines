# Eleven Million Lines You Should Know

A university course for reading code alongside classical literature, mathematics, and languages.

Eleven codebases. Orientation, not mastery. Learning to stand inside large, old, important code and find your bearings.

---

## The idea

Most programmers never read a codebase they didn't write. This course treats landmark codebases the way a literature student treats canonical texts — as objects worth sustained attention, historical study, and careful reading.

The thesis: **coding is writing augmented with electricity.** Code has styles, schools, traditions, venerated texts, living masters, and dead ones whose influence persists. The history of code is, among other things, a history of writing. This course reads it that way.

---

## The units

| # | Title | Theme |
|---|-------|-------|
| 01 | Early Unix | *Classical Coding, pt. 1* — xv6, unix-v6, Plan 9; Lions' Commentary |
| 02 | Classical Coding | *The complete stack* — C compilers, vi/vim, git; Linus Torvalds |
| 03 | Richard Stallman | *The legal and moral infrastructure of free software* — GNU, GPL, Emacs, GDB, Bison |
| 04 | Blender | *Art and technology* — the heroic story; the community buyout; DNA/RNA architecture |
| 05 | Culture and Spectacle | *Making in public* — TeX, BitTorrent, Linux, SageMath, SourceForge; skateboarding as parallel |
| 06 | Languages and Theory | *The code is the art* — BASIC, Assembly, LISP, ML/Haskell; Church, Turing, Lovelace, McCarthy |
| 07 | The Spiritual | *Mathematics that underlies the mathematics* — Grothendieck, Lawvere, Lean/Mathlib, Agda; original simplicial homology implementation |
| 08–11 | TBD | *In progress* |

---

## Two tracks

**Track A — Classical:** Unix environment, vim, command line, compile it yourself. The tools are part of the curriculum.

**Track B — Accompanied:** Any environment the student brings. More scaffolding. Honest about the tradeoff: something is lost, something is gained.

Both tracks share the same texts, the same codebases, and the same conviction that a tradition exists, here is what it looks like, and you are now in relation to it.

---

## What is in this repository

Each unit directory contains:
- A unit document (the orientation, the story, the argument)
- The codebases — cloned from public sources, checked out sparsely where size demands it
- `commentary/` — guided walks into the source
- `scratch/` — exercises, primary texts, documents for annotation

The embedded repositories (emacs, blender, gdb, etc.) are gitlinks pointing to their upstream sources. Clone them independently if you want their full history.

`meta/` holds course administration — storage sizes, the pograde assessment system (in progress).

---

## Original content

`07/scratch/simplicial_homology.py` is original to this course: a from-scratch implementation of simplicial homology over ℤ/2ℤ, computing Betti numbers for the circle, sphere, torus, RP², and more. It exists nowhere else. Verified correct; ∂²=0 confirmed; all Euler characteristic checks pass.

More original content in development.

---

## Status

Active development. Units 01–07 are seeded. Units 08–11 are open.

This is being built in public because making in public changes what gets made.

---

## Name

*Eleven Million Lines You Should Know* — eleven codebases, each one a world.
