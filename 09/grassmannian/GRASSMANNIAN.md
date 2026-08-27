# Grassmannians — Special Topic

*Why the geometry of 3D rendering has a name, and what that name reveals.*

---

## The question behind the question

When Carmack writes a BSP tree, he is repeatedly choosing a hyperplane to split space.
When the renderer normalizes a vector, it is projecting onto a sphere.
When the camera defines a view frustum, it is selecting a projective frame.

These are not ad hoc operations. They are instances of a single mathematical structure:
the **Grassmannian**.

The Grassmannian is the space of all linear subspaces of a fixed dimension inside
a vector space. It is where the geometry of Quake actually lives, one level of
abstraction above the code.

---

## Definition

The **Grassmannian G(k, n)** is the set of all k-dimensional subspaces of ℝⁿ.

Special cases, all of them familiar:

| G(k, n)  | What it is                                            | Dimension |
|----------|-------------------------------------------------------|-----------|
| G(1, 2)  | Lines through the origin in ℝ² = RP¹ ≅ S¹            | 1         |
| G(1, 3)  | Lines through the origin in ℝ³ = RP²                  | 2         |
| G(2, 3)  | Planes through the origin in ℝ³ ≅ RP² (by duality)   | 2         |
| G(1, 4)  | Lines through the origin in ℝ⁴ = RP³                 | 3         |
| G(2, 4)  | Planes through the origin in ℝ⁴                       | 4         |
| G(n−1,n) | Hyperplanes through the origin in ℝⁿ ≅ RP^{n−1}      | n−1       |

The dimension of G(k, n) is k(n − k).

Note: RP¹ ≅ S¹, RP³ ≅ SO(3)/Z₂ (the rotation group, almost). These are not curiosities.
They are load-bearing mathematical facts about 3D space.

---

## The connection to Quake

**BSP trees.** Each internal node of a BSP tree is a hyperplane that splits space.
A hyperplane through the origin in ℝ³ is an element of G(2, 3) ≅ RP².
An affine hyperplane (not necessarily through the origin) is a translate of one — a point
in the affine Grassmannian. Carmack's BSP builder is walking through this space,
choosing splits greedily.

**Normalized vectors.** The fast inverse square root computes 1/√‖v‖ so that v can be
normalized to a unit vector. Unit vectors in ℝ³ live on S², the 2-sphere. S² double-covers
RP² — every line through the origin meets the sphere in two antipodal points.
When you normalize a direction vector, you are projecting from ℝ³\{0} onto S².

**Quaternions and rotation.** Quake's physics engine represents orientations using
quaternion arithmetic. The unit quaternions form S³. The rotation group SO(3) = S³/Z₂ ≅ RP³.
The fact that RP³ = G(1, 4) means rotations in 3D space are points in a Grassmannian.

**View frustum.** A camera in 3D defines a projective frame. The space of all possible
camera positions and orientations is a fiber bundle over ℝ³ with fiber SO(3) ≅ RP³.
This is not abstract. It is the data structure the renderer uses to transform world
coordinates into screen coordinates.

---

## The Plücker embedding

Grassmannians live inside projective space via the **Plücker embedding**.

Given a k-dimensional subspace V ⊂ ℝⁿ with basis {v₁, ..., vₖ}, define:

    p(V) = v₁ ∧ v₂ ∧ ... ∧ vₖ  ∈  Λᵏ(ℝⁿ)

The result is a nonzero element of the exterior algebra, determined up to scalar —
hence a point in projective space P(Λᵏ(ℝⁿ)) ≅ RP^{C(n,k)−1}.

This is the Plücker embedding: G(k, n) ↪ RP^{C(n,k)−1}.

For G(2, 4) (planes in ℝ⁴), this is G(2, 4) ↪ RP⁵.
The image is defined by a single quadratic equation (the Plücker relation).

The Plücker embedding makes G(k, n) into an algebraic variety — a geometric object
defined by polynomial equations. This is how computer graphics encodes subspaces:
as coordinate vectors satisfying constraints.

---

## Homology of Grassmannians — Schubert calculus

This is where Unit 08 and Unit 09 meet.

Grassmannians have a beautiful cellular decomposition into **Schubert cells**,
indexed by integer partitions (equivalently, Young diagrams).

For G(k, n), the cells are indexed by partitions λ = (λ₁ ≥ λ₂ ≥ ... ≥ λₖ ≥ 0)
with λ₁ ≤ n − k. The dimension of the cell corresponding to λ is |λ| = Σ λᵢ.

**Example: G(2, 4)** (dim 4, cells in dimensions 0, 1, 2, 2, 3, 4):

| Partition λ | Cell dim | Schubert class |
|-------------|----------|----------------|
| ∅           | 0        | [pt] = 1       |
| (1)         | 1        | σ₁             |
| (2)         | 2        | σ₂             |
| (1,1)       | 2        | σ₁₁            |
| (2,1)       | 3        | σ₂₁            |
| (2,2)       | 4        | σ₂₂            |

The homology of G(2,4) over ℤ is free abelian:
H₀ = ℤ, H₁ = ℤ, H₂ = ℤ², H₃ = ℤ, H₄ = ℤ.

No torsion. This is a general fact: real Grassmannians have 2-torsion,
complex Grassmannians are torsion-free.

**Schubert calculus** is the intersection theory on these classes.
The product σ₁ · σ₁ = σ₂ + σ₁₁ in H*(G(2,4)) says: two general lines in ℝ⁴
span a plane that intersects a given plane in a point — and this is counted
by the formula above.

This connects back to Unit 07 (Grothendieck, who reformulated Schubert calculus
in K-theory) and Unit 08 (where we computed homology by hand).

---

## Grassmannians in the wild

Grassmannians are not an abstraction invented for mathematicians.
They appear wherever subspaces matter:

**Computer vision.** The space of possible camera orientations is a Grassmannian.
Structure-from-motion algorithms navigate it to recover 3D geometry from 2D images.

**Machine learning.** Principal Component Analysis finds the k-dimensional subspace
that best approximates a dataset — a point in G(k, n). Dimensionality reduction
is optimization on a Grassmannian.

**Signal processing.** Subspace methods (MUSIC algorithm for direction-of-arrival)
compute in Grassmannians. Your phone's GPS and radio use them.

**Physics.** The moduli space of instantons (solutions to the Yang-Mills equations)
is an ADHM construction over a Grassmannian. Witten's topological quantum field
theory produces Donaldson invariants from intersection theory on moduli spaces —
generalizations of Schubert calculus.

**Robotics.** The configuration space of a robot arm with joints has a natural
Grassmannian component for each joint's rotation group.

---

## The thread from Quake to here

Wolf3D (1992): cast rays through a flat grid. No subspaces, just rays.

Doom (1993): split space with hyperplanes (BSP nodes ∈ G(2,3)). Traverse front-to-back.

Quake (1996): true 3D BSP + PVS + quaternion physics + normalized vectors.
The Grassmannian structure is everywhere, unnamed.

Carmack did not need to know what a Grassmannian was to write Quake.
But Quake is computing in Grassmannians the way Jourdain spoke prose —
doing it all along without knowing the name.

Knowing the name changes what you can see next.

---

## Going further

- **Hatcher**, §4.D: Grassmannians and characteristic classes (advanced, but Hatcher is clear)
- **Milnor and Stasheff**, *Characteristic Classes* — the standard reference
- **3Blue1Brown** on the Grassmannian: search "exterior algebra" and "linear subspaces"
- **Griffiths and Harris**, *Principles of Algebraic Geometry*, Chapter 1 — Schubert calculus
  in full generality, including intersection numbers

The Plücker embedding and Schubert calculus are computable.
`08/python/` has everything needed to compute the homology of G(k,n)
if you give it the right simplicial triangulation.
That is a non-trivial exercise — and a real research direction.
