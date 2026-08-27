# Simplicial Homology — Python

A complete, tested implementation of simplicial homology over ℤ.
Built to be read. Every function does one thing.

## Run it

```bash
cd 08/python

# See all standard spaces and their homology:
python examples.py

# Run the tests:
python -m pytest tests/ -v
```

## Files, in reading order

```
simplicial.py   — SimplicialComplex: the data structure
boundary.py     — boundary_matrix(): ∂_n as an integer matrix
smith.py        — smith_factors(): invariant factors over ℤ
homology.py     — HomologyGroup, homology(), all_homology()
examples.py     — circle, sphere, torus, Klein bottle, RP^2, Möbius band
tests/          — one test class per space, checks against known answers
```

## The computation in one paragraph

A simplicial complex K is a collection of simplices (vertices, edges,
triangles, tetrahedra, ...) closed under taking faces. The n-th chain
group C_n is the free abelian group on the n-simplices. The boundary
map ∂_n: C_n → C_{n-1} sends each n-simplex to the alternating sum of
its faces. The key fact is ∂∂ = 0 — the boundary of a boundary is
always zero. Homology H_n = ker(∂_n) / im(∂_{n+1}) measures what is
in the kernel but not the image: cycles that are not boundaries. Smith
normal form over ℤ turns this into a computation.

## What the output looks like

```
──────────────────────────────────────────────────
  Torus T^2
──────────────────────────────────────────────────
  dim = 2, χ = 0
  → H_0 = ℤ
  → H_1 = ℤ^2
  → H_2 = ℤ

──────────────────────────────────────────────────
  Klein bottle
──────────────────────────────────────────────────
  dim = 2, χ = 0
  → H_0 = ℤ
  → H_1 = ℤ ⊕ ℤ/2ℤ
     H_2 = 0
```

## Extending it

To add your own space, pass a list of maximal simplices to SimplicialComplex.
Faces are generated automatically.

```python
from simplicial import SimplicialComplex
from homology import describe

# A tetrahedron (solid — contractible)
solid_tetra = SimplicialComplex([(0,1,2,3)])
describe(solid_tetra, 'Solid tetrahedron')

# Expected: H_0 = ℤ, everything else 0

# Wedge of two circles: glue two triangles at a vertex
wedge = SimplicialComplex([(0,1), (1,2), (0,2), (0,3), (3,4), (0,4)])
describe(wedge, 'Wedge S^1 ∨ S^1')
# Expected: H_0 = ℤ, H_1 = ℤ^2
```

## Dependencies

Standard library only. No numpy, no scipy.
Python 3.7+.
