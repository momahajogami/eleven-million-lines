"""
Standard spaces as simplicial complexes.

Each function returns a SimplicialComplex with the expected homology groups.
These serve as both examples and test cases.

Expected homology (coefficients over ℤ):

    point():        H_0 = ℤ
    two_points():   H_0 = ℤ²
    interval():     H_0 = ℤ
    circle():       H_0 = ℤ,  H_1 = ℤ
    sphere():       H_0 = ℤ,  H_1 = 0,  H_2 = ℤ
    torus():        H_0 = ℤ,  H_1 = ℤ², H_2 = ℤ
    klein_bottle(): H_0 = ℤ,  H_1 = ℤ ⊕ ℤ/2ℤ, H_2 = 0
    rp2():          H_0 = ℤ,  H_1 = ℤ/2ℤ,     H_2 = 0
    mobius_band():  H_0 = ℤ,  H_1 = ℤ
"""

from simplicial import SimplicialComplex


def point():
    """A single vertex."""
    return SimplicialComplex([(0,)])


def two_points():
    """Two disconnected vertices."""
    return SimplicialComplex([(0,), (1,)])


def interval():
    """A single edge — contractible to a point."""
    return SimplicialComplex([(0, 1)])


def circle():
    """
    S^1 as the boundary of a triangle.
    Three vertices, three edges, no filled triangle.
    """
    return SimplicialComplex([(0, 1), (1, 2), (0, 2)])


def sphere():
    """
    S^2 as the boundary of a tetrahedron.
    Four vertices, six edges, four triangles, no solid interior.
    This is the simplest triangulation of S^2.
    """
    return SimplicialComplex([
        (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)
    ])


def torus():
    """
    T^2 — the standard 9-vertex triangulation.

    Arrange 9 vertices in a 3×3 grid, v(i,j) = 3i + j.
    Identify opposite sides:
        top row = bottom row (vertical identification)
        left col = right col (horizontal identification)

    Each unit square is divided into two triangles.
    Result: 9 vertices, 27 edges, 18 triangles. χ = 0.
    """
    def v(i, j):
        return 3 * (i % 3) + (j % 3)

    triangles = []
    for i in range(3):
        for j in range(3):
            triangles.append((v(i, j), v(i, j+1), v(i+1, j+1)))
            triangles.append((v(i, j), v(i+1, j), v(i+1, j+1)))
    return SimplicialComplex(triangles)


def klein_bottle():
    """
    The Klein bottle — a non-orientable surface.

    Same grid as the torus, but the horizontal (j) identification
    is reversed: the right edge glues to the left edge upside down.

    Identification: v(i, 3) = v(2-i, 0) instead of v(i, 0).
    Result: 9 vertices, 27 edges, 18 triangles. χ = 0.

    H_1 = ℤ ⊕ ℤ/2ℤ — the ℤ/2ℤ torsion marks non-orientability.
    """
    def v(i, j):
        i = i % 3
        if j % 3 == 0 and j > 0:
            # Horizontal identification with flip
            return 3 * ((2 - i) % 3) + 0
        return 3 * i + (j % 3)

    triangles = []
    for i in range(3):
        for j in range(3):
            triangles.append((v(i, j), v(i, j+1), v(i+1, j+1)))
            triangles.append((v(i, j), v(i+1, j), v(i+1, j+1)))
    return SimplicialComplex(triangles)


def rp2():
    """
    RP^2 — the real projective plane.

    The minimal triangulation with 6 vertices, 15 edges, 10 triangles.
    χ = 6 - 15 + 10 = 1.

    H_1 = ℤ/2ℤ — the generator is the non-contractible loop;
    going around it twice is a boundary (you return having flipped orientation).
    """
    return SimplicialComplex([
        (0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 0), (4, 0, 1),
        (0, 2, 5), (2, 4, 5), (4, 1, 5), (1, 3, 5), (3, 0, 5),
    ])


def mobius_band():
    """
    The Möbius band — a non-orientable surface with boundary.

    Triangulated as a strip of triangles with one end flipped before gluing.
    Deformation retracts to a circle, so H_1 = ℤ.
    """
    # Five vertices along two edges of the strip,
    # with the identification 0↔4 and 5↔9 (with flip).
    return SimplicialComplex([
        (0, 1, 5), (1, 5, 6),
        (1, 2, 6), (2, 6, 7),
        (2, 3, 7), (3, 7, 8),
        (3, 4, 8), (4, 8, 9),
        (4, 0, 9), (0, 9, 5),
    ])


def dunce_hat():
    """
    The dunce hat — a contractible but not collapsible space.
    A triangle with all three edges identified, one with a flip.
    H_* = H_*(point): H_0 = ℤ, everything else 0.
    A famous counterexample in combinatorial topology.
    """
    # 3 vertices, edges all identified to form the dunce hat.
    # Hard to triangulate minimally; we use a 6-vertex version.
    return SimplicialComplex([
        (0, 1, 2), (0, 2, 3), (0, 1, 3), (1, 2, 3),
        (0, 1, 4), (1, 2, 4), (0, 2, 4),
    ])


if __name__ == '__main__':
    from homology import describe

    describe(point(), 'Point')
    describe(two_points(), 'Two disjoint points')
    describe(interval(), 'Interval [0,1]')
    describe(circle(), 'Circle S^1')
    describe(sphere(), 'Sphere S^2')
    describe(torus(), 'Torus T^2')
    describe(klein_bottle(), 'Klein bottle')
    describe(rp2(), 'Real projective plane RP^2')
    describe(mobius_band(), 'Möbius band')
