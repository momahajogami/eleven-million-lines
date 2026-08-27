# Exercises — Simplicial Homology

*Three levels. Do what you can. Come back to the rest.*

---

## Level 1 — By Hand

These can all be done with pencil and paper.
The goal is to feel the machinery before you run the code.

**1.1** Draw the simplicial complex K with:
- Vertices: 0, 1, 2, 3
- Edges: (0,1), (1,2), (2,3), (0,3)
- No triangles

What space is this? (Hint: it's a familiar one-dimensional shape.)
Compute H₀ and H₁ by reasoning geometrically, then verify with the code.

**1.2** Write out ∂₁ for the circle (the 3×3 matrix from MATHEMATICS.md).
Use row and column operations over ℤ to reduce it to diagonal form by hand.
What are the invariant factors?

**1.3** Consider a single filled triangle K = {(0,1,2)}.
This is a disk — topologically contractible.
Compute H₀, H₁, H₂ by:
(a) reasoning geometrically (what spaces are contractible to?)
(b) running `homology(SimplicialComplex([(0,1,2)]), n)` for n = 0, 1, 2

**1.4** The wedge sum S¹ ∨ S¹ is two circles sharing a single point.
Build this as a simplicial complex and compute its homology.
Expected: H₀ = ℤ, H₁ = ℤ², H₂ = 0.

**1.5** Compute the Euler characteristic of each space in the table in MATHEMATICS.md
using the formula χ = V − E + F (vertices minus edges plus triangles).
Check that it agrees with χ = β₀ − β₁ + β₂.

---

## Level 2 — Understanding

These require you to think, not just compute.

**2.1** Prove that ∂₁ ∘ ∂₂ = 0 for any simplicial complex. That is:
show that for any triangle (a,b,c), ∂₁(∂₂((a,b,c))) = 0.
The calculation is in MATHEMATICS.md. Now generalize: prove that
∂_{n-1} ∘ ∂_n = 0 for any n and any n-simplex.

*(Hint: a telescope. Most terms cancel. Figure out which ones pair up and why.)*

**2.2** The Euler-Poincaré formula says χ = Σ(−1)^n β_n.
Prove this starting from the definition β_n = dim ker ∂_n − dim im ∂_{n+1}
and the rank-nullity theorem (dim ker + dim im = dim domain).

*(This proof is the same over ℤ as over ℚ, if you're careful.)*

**2.3** H₀ = ℤ^c where c is the number of connected components.
Prove this from the definition. (What is ker ∂₀? What is im ∂₁?)

**2.4** A simplicial complex K is **acyclic** if H_n(K) = 0 for all n > 0.
The cone over K (add a new vertex v connected to everything in K) is always acyclic.
Prove this.

*(This gives a practical way to kill all homology.)*

**2.5** The ℤ/2ℤ in H₁(RP²) corresponds to what geometric fact?
Describe the generator of H₁(RP²) as a specific cycle.
Why is twice this cycle a boundary? What boundary is it?

---

## Level 3 — Programming

These extend the code.

**3.1** Add a method `SimplicialComplex.is_manifold(n)` that checks whether
K is a topological n-manifold: every (n-1)-simplex must be the face of
exactly 1 or 2 n-simplices (1 on the boundary, 2 in the interior).

Test it on the sphere (manifold), the torus (manifold), and a figure-8
(not a manifold at the pinch point).

**3.2** Implement homology with coefficients in ℤ/2ℤ. Over ℤ/2ℤ:
- There is no sign (−1 = 1)
- Smith normal form becomes Gaussian elimination mod 2
- No torsion is possible (ℤ/2ℤ is a field)

Compare RP² over ℤ (H₁ = ℤ/2ℤ) with RP² over ℤ/2ℤ (H₁ = ℤ/2ℤ,
but also H₂ = ℤ/2ℤ — the top class appears because we can no longer
detect non-orientability by sign).

**3.3** Implement the **suspension** operation: given a simplicial complex K,
the suspension SK is formed by adding two new vertices v₊ and v₋,
and for each simplex σ in K, adding cones (σ ∪ {v₊}) and (σ ∪ {v₋}).

Verify: if H_n(K) = G, then H_{n+1}(SK) = G. (Suspension shifts homology up by one.)

Test: SK¹ = S², SK² = S³ (well, a triangulated version).

**3.4** Implement **simplicial maps** and their induced maps on homology.

A simplicial map f: K → L sends each simplex of K to a simplex of L
(possibly of lower dimension) and extends linearly to chain groups.
The induced map f_* : H_n(K) → H_n(L) sends cycles to cycles and
boundaries to boundaries.

Test: the constant map K → {point} induces the zero map on H_n for n > 0.

**3.5** (Hard) Implement the **Mayer-Vietoris sequence**.

If K = A ∪ B where A, B are subcomplexes with A ∩ B = C, there is a
long exact sequence:

```
... → H_n(C) → H_n(A) ⊕ H_n(B) → H_n(K) → H_{n-1}(C) → ...
```

Use it to compute H_*(S²) by writing S² = upper hemisphere ∪ lower hemisphere,
where the intersection is the equatorial circle.

---

## A note on difficulty

Exercise 2.2 (Euler-Poincaré) looks like algebra but is actually counting.
If you get stuck, write out the long exact sequence for a small complex.

Exercise 3.5 (Mayer-Vietoris) is a real theorem. Implementing it means
computing the connecting homomorphism, which requires tracking the
Smith form transformation matrices (U and V, not just D). That is
the next step in the implementation beyond what this unit provides.

The gap between "I can compute homology" and "I understand homology"
is closed by exercises like these, not by reading more theory.
The reading tells you what to look for. The computing is the looking.
