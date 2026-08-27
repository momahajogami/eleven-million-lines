"""
Tests for the simplicial homology computation.

Each test checks a known space against its known homology groups.
These are the canonical examples from algebraic topology.

Run with: python -m pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from simplicial import SimplicialComplex
from boundary import boundary_matrix, verify_boundary_squared_zero
from smith import smith_factors, rank
from homology import homology, all_homology, euler_characteristic_from_homology
from examples import (
    point, two_points, interval, circle, sphere,
    torus, klein_bottle, rp2, mobius_band
)


# ── Smith Normal Form ─────────────────────────────────────────────────────────

class TestSmith:
    def test_zero_matrix(self):
        assert smith_factors([[0, 0], [0, 0]]) == []

    def test_identity(self):
        assert smith_factors([[1, 0], [0, 1]]) == [1, 1]

    def test_diagonal(self):
        # Smith form requires d_1 | d_2. Since 2∤3, diag(2,3) → [1,6].
        # Z/2Z ⊕ Z/3Z ≅ Z/6Z by the Chinese Remainder Theorem.
        assert smith_factors([[2, 0], [0, 3]]) == [1, 6]

    def test_rank_1(self):
        assert rank([[1, 2], [2, 4]]) == 1

    def test_2x3(self):
        # Matrix with rank 2 and torsion
        M = [[1, 0, 0], [0, 2, 0]]
        factors = smith_factors(M)
        assert factors == [1, 2]

    def test_torsion(self):
        # A matrix whose Smith form has a factor of 2
        M = [[2, 0], [0, 2]]
        factors = smith_factors(M)
        assert factors == [2, 2]

    def test_gcd_needed(self):
        # Smith form requires GCD computation, not just division
        M = [[2, 3], [4, 6]]
        factors = smith_factors(M)
        assert len(factors) == 1
        assert factors[0] == 1  # gcd(2,3,4,6)=1, rank 1

    def test_empty(self):
        assert smith_factors([]) == []
        assert smith_factors([[]]) == []


# ── Boundary Maps ─────────────────────────────────────────────────────────────

class TestBoundary:
    def test_circle_boundary_squared_zero(self):
        assert verify_boundary_squared_zero(circle())

    def test_sphere_boundary_squared_zero(self):
        assert verify_boundary_squared_zero(sphere())

    def test_torus_boundary_squared_zero(self):
        assert verify_boundary_squared_zero(torus())

    def test_rp2_boundary_squared_zero(self):
        assert verify_boundary_squared_zero(rp2())

    def test_boundary_matrix_edge(self):
        # ∂_1 of a single edge (0,1): rows=vertices, cols=edges
        K = SimplicialComplex([(0, 1)])
        M = boundary_matrix(K, 1)
        # Should be [[-1], [1]]: vertex 0 gets -1, vertex 1 gets +1
        assert len(M) == 2
        assert len(M[0]) == 1
        col = sorted(M[i][0] for i in range(2))
        assert col == [-1, 1]

    def test_boundary_dim_zero(self):
        K = circle()
        assert boundary_matrix(K, 0) == []


# ── Homology: Simple Spaces ───────────────────────────────────────────────────

class TestPoint:
    def test_h0(self):
        g = homology(point(), 0)
        assert g.betti == 1
        assert g.torsion == []


class TestTwoPoints:
    def test_h0(self):
        g = homology(two_points(), 0)
        assert g.betti == 2
        assert g.torsion == []


class TestInterval:
    def test_h0(self):
        g = homology(interval(), 0)
        assert g.betti == 1
    def test_h1(self):
        g = homology(interval(), 1)
        assert g.betti == 0
        assert g.torsion == []


# ── Homology: The Classics ────────────────────────────────────────────────────

class TestCircle:
    """S^1: the archetypal space with a one-dimensional hole."""
    def test_h0(self):
        g = homology(circle(), 0)
        assert g.betti == 1

    def test_h1(self):
        g = homology(circle(), 1)
        assert g.betti == 1
        assert g.torsion == []

    def test_euler(self):
        assert circle().euler_characteristic() == 0


class TestSphere:
    """S^2: connected, no 1-holes, one 2-void."""
    def test_h0(self):
        assert homology(sphere(), 0).betti == 1

    def test_h1(self):
        g = homology(sphere(), 1)
        assert g.betti == 0
        assert g.torsion == []

    def test_h2(self):
        g = homology(sphere(), 2)
        assert g.betti == 1
        assert g.torsion == []

    def test_euler(self):
        assert sphere().euler_characteristic() == 2


class TestTorus:
    """T^2: genus-1 surface, two independent loops, one void."""
    def test_h0(self):
        assert homology(torus(), 0).betti == 1

    def test_h1(self):
        g = homology(torus(), 1)
        assert g.betti == 2
        assert g.torsion == []

    def test_h2(self):
        g = homology(torus(), 2)
        assert g.betti == 1
        assert g.torsion == []

    def test_euler(self):
        assert torus().euler_characteristic() == 0

    def test_euler_from_betti(self):
        assert euler_characteristic_from_homology(torus()) == 0


class TestKleinBottle:
    """Klein bottle: non-orientable, torsion in H_1."""
    def test_h0(self):
        assert homology(klein_bottle(), 0).betti == 1

    def test_h1(self):
        g = homology(klein_bottle(), 1)
        assert g.betti == 1
        assert 2 in g.torsion

    def test_h2(self):
        g = homology(klein_bottle(), 2)
        assert g.betti == 0

    def test_euler(self):
        assert klein_bottle().euler_characteristic() == 0


class TestRP2:
    """RP^2: the projective plane. Pure torsion in H_1."""
    def test_h0(self):
        assert homology(rp2(), 0).betti == 1

    def test_h1(self):
        g = homology(rp2(), 1)
        assert g.betti == 0
        assert g.torsion == [2]

    def test_h2(self):
        g = homology(rp2(), 2)
        assert g.betti == 0
        assert g.torsion == []

    def test_euler(self):
        assert rp2().euler_characteristic() == 1


class TestMobiusBand:
    """Möbius band: non-orientable, deformation retracts to a circle."""
    def test_h0(self):
        assert homology(mobius_band(), 0).betti == 1

    def test_h1(self):
        g = homology(mobius_band(), 1)
        assert g.betti == 1
        assert g.torsion == []


# ── Euler Characteristic Consistency ─────────────────────────────────────────

class TestEulerConsistency:
    """χ = Σ(-1)^n β_n must agree with the simplicial count."""
    @pytest.mark.parametrize("space,name", [
        (point(), 'point'),
        (interval(), 'interval'),
        (circle(), 'circle'),
        (sphere(), 'sphere'),
        (torus(), 'torus'),
        (rp2(), 'rp2'),
        (mobius_band(), 'mobius'),
    ])
    def test_euler_agrees(self, space, name):
        chi_simplicial = space.euler_characteristic()
        chi_homology = euler_characteristic_from_homology(space)
        assert chi_simplicial == chi_homology, (
            f"{name}: χ_simplicial={chi_simplicial}, χ_homology={chi_homology}"
        )
