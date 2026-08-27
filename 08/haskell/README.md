# Simplicial Homology — Haskell

The same computation as `08/python/`, wearing different clothes.

Read both. The mathematics does not change. The way of thinking does.

## Build and run

```bash
cd 08/haskell
cabal build
cabal run
```

Or, if you prefer GHCi for exploration:

```bash
ghci -i. Main.hs
:load Main
main
```

## What Haskell adds

**Types as documentation.** In Python, a simplex is just a tuple.
In Haskell, `type Simplex = [Int]` is a declaration — the code
announces what things are, not just what they do.

**Purity.** Every function here is a pure function. `smithFactors` maps
a matrix to a list of integers with no side effects, no mutation, no
hidden state. The boundary of a boundary is still zero, and the type
checker will enforce it.

**Algebraic data types.** `HomologyGroup` is a product type — it
carries its dimension, Betti number, and torsion coefficients as a
single value. Pattern matching on it is exhaustive. You cannot forget
the torsion case.

## The key insight the types reveal

In Python, `boundary_matrix` returns `[[int]]` — a fact about
representation. In Haskell, if you wrote a proper module with full types,
you would write:

```haskell
boundaryMap :: ChainGroup n -> ChainGroup (n-1) -> Matrix Int
```

The chain complex structure — that ∂_n goes from C_n to C_{n-1} — would
live in the types, not just in the comments.

This is what dependent types (Agda, Lean) push further: the fact
that ∂∂ = 0 can be a *type-level theorem*, not a runtime check.

## Reading order

```
Simplicial.hs   — types and complex construction
Boundary.hs     — boundary matrices from simplices
Smith.hs        — Smith normal form over ℤ
Homology.hs     — HomologyGroup and the main computation
Examples.hs     — standard spaces
Main.hs         — runs everything and checks consistency
```
