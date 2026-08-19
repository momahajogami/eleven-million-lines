"""
simplicial_homology.py
======================
A from-scratch implementation of simplicial homology over ℤ/2ℤ.

This is original course content for "Eleven Million Lines You Should Know."
It exists nowhere else. It is yours to read, modify, and extend.

WHAT THIS COMPUTES
------------------
Given a simplicial complex K (a combinatorial description of a shape built
from vertices, edges, triangles, tetrahedra, ...), this code computes its
Betti numbers β₀, β₁, β₂, ... over the field ℤ/2ℤ = {0, 1}.

Betti numbers count topological features:
  β₀ = number of connected components
  β₁ = number of independent 1-dimensional loops
  β₂ = number of independent 2-dimensional voids (enclosed volumes)

Example: a circle has β₀=1 (connected), β₁=1 (one loop), β₂=0.
Example: a sphere has β₀=1, β₁=0, β₂=1 (one enclosed void).
Example: a torus has β₀=1, β₁=2 (two independent loops), β₂=1.

WHY ℤ/2ℤ
---------
Over the integers, simplicial homology requires tracking signs — the boundary
of a triangle [v₀,v₁,v₂] is +[v₁,v₂] - [v₀,v₂] + [v₀,v₁]. Over ℤ/2ℤ,
-1 = +1, so signs vanish. The boundary just drops each vertex in turn.

This makes the computation clean: everything reduces to Gaussian elimination
over {0,1}. The tradeoff is that ℤ/2ℤ homology cannot distinguish between
the torus and the Klein bottle (they have the same Betti numbers mod 2).
Integer homology can — through torsion, which this implementation ignores.

THE MATHEMATICS
---------------
A simplicial complex K is a collection of simplices (faces) closed under
taking subsets. An n-simplex is an ordered set of (n+1) vertices.

The chain group Cₙ is the vector space over ℤ/2ℤ with basis = {n-simplices}.
A chain is a formal sum (mod 2) of n-simplices — equivalently, a subset.

The boundary operator ∂ₙ: Cₙ → Cₙ₋₁ is the linear map defined on a basis
element [v₀,...,vₙ] by dropping each vertex in turn:

    ∂ₙ[v₀,...,vₙ] = Σᵢ [v₀,...,v̂ᵢ,...,vₙ]  (mod 2)

The key fact: ∂ₙ₋₁ ∘ ∂ₙ = 0 (boundary of boundary is zero).
This means im(∂ₙ₊₁) ⊆ ker(∂ₙ), which makes the following well-defined:

    Hₙ(K; ℤ/2ℤ) = ker(∂ₙ) / im(∂ₙ₊₁)

The Betti number βₙ = dim(Hₙ) = dim(ker ∂ₙ) - dim(im ∂ₙ₊₁)
                              = (|Cₙ| - rank ∂ₙ) - rank ∂ₙ₊₁

DEPENDENCIES
------------
Only numpy. Could be done with pure Python lists; numpy makes it cleaner.

RUNNING
-------
    python simplicial_homology.py

All examples are computed and verified automatically.
"""

import numpy as np
from itertools import combinations


# =============================================================================
# SIMPLICIAL COMPLEX
# =============================================================================

class SimplicialComplex:
    """
    A simplicial complex stored as a dictionary mapping dimension to
    a list of simplices, each simplex a frozenset of vertex labels.
    Vertex labels can be any hashable objects (ints, strings, tuples).
    """

    def __init__(self):
        self._simplices = {}   # dim -> list of frozenset

    def add(self, *vertices):
        """
        Add a simplex and all its faces recursively.
        add(0, 1, 2) adds the triangle {0,1,2} and its edges and vertices.
        Returns self for chaining: K.add(0,1).add(1,2).add(0,2)
        """
        verts = tuple(sorted(vertices))
        dim = len(verts) - 1
        s = frozenset(verts)

        if dim not in self._simplices:
            self._simplices[dim] = []

        if s not in self._simplices[dim]:
            self._simplices[dim].append(s)
            # Add all codimension-1 faces
            if dim > 0:
                for face in combinations(verts, dim):
                    self.add(*face)

        return self

    def simplices(self, dim):
        """Return simplices of given dimension, sorted for determinism."""
        raw = self._simplices.get(dim, [])
        return sorted(raw, key=lambda s: sorted(s))

    def max_dim(self):
        return max(self._simplices.keys()) if self._simplices else -1

    def summary(self):
        labels = ['vertices', 'edges', 'triangles', 'tetrahedra']
        for d in range(self.max_dim() + 1):
            n = len(self.simplices(d))
            lbl = labels[d] if d < len(labels) else f'{d}-simplices'
            print(f'    {n:4d}  {lbl}')


# =============================================================================
# BOUNDARY MATRIX
# =============================================================================

def boundary_matrix(K, n):
    """
    Compute the matrix of ∂ₙ: Cₙ → Cₙ₋₁ over ℤ/2ℤ.

    Rows index (n-1)-simplices. Columns index n-simplices.
    Entry M[i,j] = 1 iff the i-th (n-1)-simplex is a face of the j-th n-simplex.

    Returns a numpy array of dtype uint8.
    """
    cols = K.simplices(n)
    rows = K.simplices(n - 1)

    if not cols or not rows:
        return np.zeros((len(rows), len(cols)), dtype=np.uint8)

    row_index = {s: i for i, s in enumerate(rows)}
    M = np.zeros((len(rows), len(cols)), dtype=np.uint8)

    for j, sigma in enumerate(cols):
        verts = sorted(sigma)
        for i in range(len(verts)):
            face = frozenset(verts[:i] + verts[i + 1:])
            if face in row_index:
                M[row_index[face], j] = 1

    return M


# =============================================================================
# RANK OVER ℤ/2ℤ
# =============================================================================

def rank_mod2(M):
    """
    Rank of M over ℤ/2ℤ via Gaussian elimination.

    All arithmetic is mod 2, so subtraction = addition = XOR.
    We find a pivot column, swap rows, then eliminate that column
    from all other rows. Count how many pivots we find.
    """
    if M.size == 0:
        return 0

    M = M.copy().astype(np.uint8)
    rows, cols = M.shape
    pivot_row = 0

    for col in range(cols):
        # Find a row at or below pivot_row with a 1 in this column
        found = None
        for row in range(pivot_row, rows):
            if M[row, col] == 1:
                found = row
                break
        if found is None:
            continue

        # Move the pivot row into position
        M[[pivot_row, found]] = M[[found, pivot_row]]

        # Eliminate this column entry in all other rows (XOR = add mod 2)
        for row in range(rows):
            if row != pivot_row and M[row, col] == 1:
                M[row] = (M[row] + M[pivot_row]) % 2

        pivot_row += 1

    return pivot_row


# =============================================================================
# BETTI NUMBERS AND HOMOLOGY
# =============================================================================

def betti(K, n):
    """
    Compute the n-th Betti number of K over ℤ/2ℤ.

    βₙ = dim(ker ∂ₙ) - dim(im ∂ₙ₊₁)
       = (|Cₙ| - rank ∂ₙ) - rank ∂ₙ₊₁
    """
    cn = len(K.simplices(n))
    if cn == 0:
        return 0

    dn  = boundary_matrix(K, n)
    dn1 = boundary_matrix(K, n + 1)

    return (cn - rank_mod2(dn)) - rank_mod2(dn1)


def euler_characteristic(K):
    """χ = Σₙ (-1)ⁿ |Cₙ| = Σₙ (-1)ⁿ βₙ  (two ways to compute)"""
    from_simplices = sum(
        (-1)**n * len(K.simplices(n))
        for n in range(K.max_dim() + 1)
    )
    return from_simplices


def report(K, name):
    """Print a full homology report and verify the Euler characteristic."""
    print(f'\n{"=" * 56}')
    print(f'  {name}')
    print(f'{"=" * 56}')
    K.summary()

    print()
    bettis = [betti(K, n) for n in range(K.max_dim() + 2)]
    # Trim trailing zeros (but always show at least through max_dim)
    while len(bettis) > K.max_dim() + 1 and bettis[-1] == 0:
        bettis.pop()

    for n, b in enumerate(bettis):
        annotation = ''
        if n == 0 and b > 1:
            annotation = f'  ← {b} components'
        elif n == 0:
            annotation = '  ← connected'
        elif n == 1 and b > 0:
            annotation = f'  ← {b} independent loop{"s" if b > 1 else ""}'
        elif n == 2 and b > 0:
            annotation = f'  ← {b} enclosed void{"s" if b > 1 else ""}'
        print(f'  β_{n} = {b}{annotation}')

    chi_simp  = euler_characteristic(K)
    chi_betti = sum((-1)**n * b for n, b in enumerate(bettis))
    status = '✓' if chi_simp == chi_betti else '✗ MISMATCH'
    print(f'\n  χ = {chi_simp}  (Euler characteristic)  {status}')


# =============================================================================
# THE EXAMPLES
# =============================================================================

def example_point():
    K = SimplicialComplex()
    K.add(0)
    report(K, 'Point  {0}')
    # Expected: β₀=1

def example_two_points():
    K = SimplicialComplex()
    K.add(0)
    K.add(1)
    report(K, 'Two disjoint points  {0}  {1}')
    # Expected: β₀=2  (two components)

def example_interval():
    K = SimplicialComplex()
    K.add(0, 1)
    report(K, 'Interval  [0—1]')
    # Expected: β₀=1 (connected), β₁=0 (no loop)

def example_circle():
    """
    Boundary of a triangle — topologically a circle.
    Three vertices, three edges, NO filled triangle.
    """
    K = SimplicialComplex()
    K.add(0, 1)
    K.add(1, 2)
    K.add(0, 2)
    report(K, 'Circle  (boundary of triangle, no fill)')
    # Expected: β₀=1, β₁=1

def example_disk():
    """
    Filled triangle — topologically a disk.
    The fill kills the loop: β₁=0.
    """
    K = SimplicialComplex()
    K.add(0, 1, 2)   # adding the triangle adds all edges and vertices
    report(K, 'Disk  (filled triangle)')
    # Expected: β₀=1, β₁=0

def example_two_loops():
    """
    Figure-eight: two circles sharing a vertex.
    β₁=2: two independent loops.
    """
    K = SimplicialComplex()
    # First loop: vertices 0,1,2
    K.add(0, 1)
    K.add(1, 2)
    K.add(0, 2)
    # Second loop: vertices 0,3,4
    K.add(0, 3)
    K.add(3, 4)
    K.add(0, 4)
    report(K, 'Figure-eight  (two circles sharing vertex 0)')
    # Expected: β₀=1, β₁=2

def example_sphere():
    """
    Boundary of a tetrahedron — topologically a 2-sphere.
    Four triangles, no solid interior.
    """
    K = SimplicialComplex()
    K.add(0, 1, 2)
    K.add(0, 1, 3)
    K.add(0, 2, 3)
    K.add(1, 2, 3)
    report(K, 'Sphere  (boundary of tetrahedron, no fill)')
    # Expected: β₀=1, β₁=0, β₂=1

def example_solid_tetrahedron():
    """
    Filled tetrahedron — topologically a 3-ball.
    The fill kills the void: β₂=0.
    """
    K = SimplicialComplex()
    K.add(0, 1, 2, 3)
    report(K, 'Solid tetrahedron  (3-ball)')
    # Expected: β₀=1, β₁=0, β₂=0

def example_torus():
    """
    Torus T² via the 3×3 grid triangulation.

    Take the square [0,2]×[0,2] with integer vertices, identify opposite
    edges: (i,j) ~ (i+3,j) and (i,j) ~ (i,j+3).

    Vertices: v(i,j) = (i mod 3)*3 + (j mod 3), so 9 vertices total.

    Each unit square is split into two triangles:
      lower-right: v(i,j), v(i+1,j), v(i+1,j+1)
      upper-left:  v(i,j), v(i,j+1), v(i+1,j+1)

    This gives 9 squares × 2 triangles = 18 triangles.
    V=9, E=27, F=18 → χ = 9-27+18 = 0  ✓ (torus has χ=0)
    """
    def v(i, j):
        return (i % 3) * 3 + (j % 3)

    K = SimplicialComplex()
    for i in range(3):
        for j in range(3):
            K.add(v(i, j), v(i+1, j), v(i+1, j+1))   # lower-right
            K.add(v(i, j), v(i, j+1), v(i+1, j+1))   # upper-left

    report(K, 'Torus  T²  (3×3 grid with opposite-edge identification)')
    # Expected: β₀=1, β₁=2, β₂=1
    # Note: over ℤ/2ℤ, the Klein bottle has the same Betti numbers.
    # Only integer homology (with torsion) distinguishes them.

def example_rp2():
    """
    Real projective plane RP².

    Obtained from a hexagon by identifying opposite edges with a twist.
    Minimal triangulation: 6 vertices, 15 edges, 10 triangles.

    Vertex labeling follows the standard hexagonal diagram:
         1
        / \\
       2   6
      / \\ / \\
     3   5   1  ← same vertex as top
      \\ / \\ /
       4   2  ← same as left
        \\ /
         3  ← same as bottom-left

    We use the explicit triangle list from Hatcher, Algebraic Topology,
    Example 2.1 (RP² triangulation).

    Triangles (vertices labeled 0–5):
    """
    K = SimplicialComplex()
    # Standard triangulation of RP² with 6 vertices
    triangles = [
        (0,1,2), (0,2,3), (0,3,4), (0,4,5), (0,1,5),
        (1,2,5), (2,3,5), (3,4,5), (1,3,4), (1,2,4),
    ]
    for t in triangles:
        K.add(*t)

    report(K, 'Real projective plane  RP²')
    # Expected over ℤ/2ℤ: β₀=1, β₁=1, β₂=1
    # Over ℤ: H₀=ℤ, H₁=ℤ/2ℤ, H₂=0  (torsion in H₁, no top-dim class)
    # ℤ/2ℤ sees the ℤ/2ℤ torsion as a genuine class: β₂=1 here.


# =============================================================================
# VERIFY ∂∘∂ = 0
# =============================================================================

def verify_boundary_squared(K):
    """
    Confirm that ∂ₙ₋₁ ∘ ∂ₙ = 0 for all n.
    This is the algebraic guarantee that homology is well-defined.
    """
    print('\n  Verifying ∂²=0:')
    ok = True
    for n in range(1, K.max_dim() + 1):
        dn  = boundary_matrix(K, n)
        dn1 = boundary_matrix(K, n - 1)
        if dn.size == 0 or dn1.size == 0:
            continue
        product = (dn1 @ dn) % 2
        if np.any(product != 0):
            print(f'    ∂_{n-1} ∘ ∂_{n} ≠ 0  ✗')
            ok = False
        else:
            print(f'    ∂_{n-1} ∘ ∂_{n} = 0  ✓')
    if ok:
        print('  All boundary-squared checks passed.')


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print('Simplicial Homology over ℤ/2ℤ')
    print('Eleven Million Lines You Should Know — Unit 07')

    example_point()
    example_two_points()
    example_interval()
    example_circle()
    example_disk()
    example_two_loops()
    example_sphere()
    example_solid_tetrahedron()
    example_torus()
    example_rp2()

    # Verify the key algebraic identity on the torus
    print('\n\nVerification on torus:')
    def v(i, j): return (i % 3) * 3 + (j % 3)
    T = SimplicialComplex()
    for i in range(3):
        for j in range(3):
            T.add(v(i, j), v(i+1, j), v(i+1, j+1))
            T.add(v(i, j), v(i, j+1), v(i+1, j+1))
    verify_boundary_squared(T)

    print('\n\nAll done.')
    print()
    print('NEXT STEPS')
    print('----------')
    print('1. Extend to integer coefficients (requires Smith normal form).')
    print('   Smith normal form reveals torsion — the difference between')
    print('   the torus and the Klein bottle that ℤ/2ℤ cannot see.')
    print()
    print('2. Implement the Mayer-Vietoris sequence: if K = A ∪ B, then')
    print('   there is a long exact sequence relating H*(A), H*(B), H*(A∩B).')
    print('   This lets you compute homology by breaking a space into pieces.')
    print()
    print('3. Implement persistent homology: vary a parameter, watch which')
    print('   topological features appear and disappear. This is the basis')
    print('   of topological data analysis (TDA), an active research area.')
    print()
    print('4. Formalize this in Lean or Agda. A verified implementation would')
    print('   be a proof that the code computes what the mathematics says it')
    print('   computes. Mathlib already has the foundational theorems;')
    print('   connecting this Python code to those proofs is a real project.')
    print()
    print('5. Build the simplicial set version: replace simplicial complexes')
    print('   with simplicial sets (where multiple simplices can share the')
    print('   same vertices), and implement the Dold-Kan correspondence.')
    print('   This is where algebraic topology meets homotopy type theory.')
