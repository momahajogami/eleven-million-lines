# Unit 08 — Simplicial Homology by Hand

Build the machinery of simplicial homology from scratch, in multiple languages, with markdown as the persistent thinking layer.

---

## The Central Idea

The mathematics lives in `.md` files. The code is its expression.

You write down what a simplicial complex is — vertices, edges, faces, the boundary maps — in plain markdown. That file persists. Tomorrow you open it in a different language and implement the same mathematics again. The markdown is what crosses languages the way `CLAUDE.md` crosses sessions.

Students see that the topology is not in Python or Haskell. It was there before either existed. The code is just a way of asking the mathematics to run.

---

## What We Build

A simplicial complex Δ, defined by its faces:
- 0-simplices (vertices): [0], [1], [2], [3]
- 1-simplices (edges): [0,1], [1,2], [0,2], [2,3]
- 2-simplices (triangles): [0,1,2]

The boundary maps:
- ∂₂: C₂ → C₁  (boundary of a triangle is its three edges, with signs)
- ∂₁: C₁ → C₀  (boundary of an edge is its two endpoints, with signs)

The chain complex:
```
0 → C₂ → C₁ → C₀ → 0
```

Homology groups:
- H₀ = ker ∂₀ / im ∂₁   (connected components)
- H₁ = ker ∂₁ / im ∂₂   (independent loops)
- H₂ = ker ∂₂ / im ∂₃   (enclosed voids)

For the example above: H₀ = ℤ, H₁ = ℤ, H₂ = 0. One component, one loop (the edge [2,3] dangles without closing).

---

## The Language Sequence

### Day 1 — Python
Dictionaries and lists. Boundary maps as matrices. Gaussian elimination over ℤ by hand (or numpy for the arithmetic, not the concept). Readable, fast to write, easy to inspect.

### Day 2 — Haskell
Types as contracts. `data Simplex`, `newtype ChainGroup`, `boundaryMap :: Simplex -> [(Int, Simplex)]`. The type system makes the mathematical structure explicit in a way Python's duck typing cannot. The same math, wearing different clothes — and the clothes are informative.

### Day 3 (optional) — C
No abstractions provided. Build everything from scratch. Feel what the Python and Haskell hid.

### Day 4 (optional) — Lean / Agda
The proof *is* the program. Homology as a verified computation. Connects to Unit 07.

---

## The Markdown Thinking Layer

Each implementation session starts with the same `.md` file — this one, or a version of it — and ends with the student having read the math, written the code, and seen the math survive the translation.

The `.md` file does not change. The language does. That is the lesson.

This mirrors how a working mathematician operates: the ideas are in the notebook, the implementations are in the tools. The notebook is primary.

---

## Paired Texts and Context

- **Hatcher, *Algebraic Topology*, Chapter 2** — standard reference; free PDF from Hatcher's website
- **Euler's 1758 paper** — the Euler characteristic discovered while counting vertices, edges, and faces of polyhedra. The first step toward homology, written before the word existed.
- **Emmy Noether** — who first saw that the boundary operation should be thought of algebraically, not geometrically. The chain complex is her idea. She did not publish it; her students did. Worth knowing.

---

## Connection to Unit 07

Unit 07 ends with `simplicial_homology.py` — a library doing the computation. Unit 08 asks: what if we wrote that ourselves? And then: what if we wrote it in Haskell? And then: what changes?

The answer is: nothing mathematical changes. Everything about how we *think* about it changes. That gap is the unit.

---

## Consideration: Quake (alternative or future slot)

Carmack's Quake engine — BSP trees, fast inverse square root, real-time 3D under constraint — is the natural counterweight to this unit. Abstract mathematics versus visceral engineering. Both are in the repo tradition; both reward close reading. Quake may belong in 09 for exactly that reason: the contrast across adjacent units would be striking.

See `BRAINSTORM.md` for fuller Quake notes.
