# Tetris — a readable implementation

**Run:** `python3 tetris.py`
**Controls:** `a`/`d` move, `w` rotate, `s` drop, `q` quit

This implementation is meant to be read, not just played. It is ~120 lines. Every function does one thing. The data model is plain: a 2D list for the board, a list of (row, col) offsets for each piece.

## What to read

**The pieces** — seven tetrominoes defined as offset lists. No matrices, no magic numbers. Just coordinates.

**`rotate()`** — 90-degree clockwise rotation in four lines. The trick: `(r, c) → (c, -r)`, then normalize back to the origin. This is a 2D linear transformation written by hand.

**`fits()`** — collision detection. Check every cell of the piece against the board and the walls. Simple and total.

**`clear_lines()`** — the Pajitnov mechanic. Find full rows, remove them, insert empty rows at the top. The list manipulation *is* the gravity.

**`main()`** — the game loop. Read input, apply gravity on a timer, draw, repeat. Every game loop in history is a variation on this structure.

## The historical note

Pajitnov wrote the original in 1984 on an Electronika 60 — a Soviet terminal with no graphics. The pieces were drawn with bracket characters. This implementation uses `[]` for the same reason: it is closer to the original than colored blocks would be.

The original source is not publicly available. This is a clean-room implementation written for readability.
