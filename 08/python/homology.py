"""
Simplicial homology groups.

H_n(K) = ker(∂_n) / im(∂_{n+1})

The computation uses Smith normal form:

    Given boundary matrices ∂_n and ∂_{n+1}:
    - rank(∂_n) = r_n  (from Smith factors of ∂_n)
    - rank(∂_{n+1}) = r_{n+1}
    - number of n-simplices = k_n

    Then:
        β_n = k_n - r_n - r_{n+1}          (Betti number: rank of free part)
        torsion: Z/d_iZ for each invariant factor d_i > 1 of ∂_{n+1}

The Betti number β_n counts independent n-dimensional holes.
Torsion arises in non-orientable spaces (real projective plane, Klein bottle).
"""

from dataclasses import dataclass, field
from typing import List
from boundary import boundary_matrix
from smith import smith_factors, rank as matrix_rank


@dataclass
class HomologyGroup:
    """
    Represents H_n = Z^β ⊕ Z/d_1Z ⊕ ... ⊕ Z/d_kZ.

    betti: the rank of the free part (number of independent holes)
    torsion: list of integers d_i > 1 (torsion coefficients)
    """
    dim: int
    betti: int
    torsion: List[int] = field(default_factory=list)

    def is_trivial(self):
        return self.betti == 0 and not self.torsion

    def __str__(self):
        parts = []
        if self.betti == 1:
            parts.append('ℤ')
        elif self.betti > 1:
            parts.append(f'ℤ^{self.betti}')
        for d in self.torsion:
            parts.append(f'ℤ/{d}ℤ')
        return ' ⊕ '.join(parts) if parts else '0'

    def __repr__(self):
        return f'H_{self.dim} = {self}'


def homology(K, n):
    """Compute H_n of simplicial complex K."""
    simplices_n = K.simplices(n)
    k_n = len(simplices_n)

    if k_n == 0:
        return HomologyGroup(dim=n, betti=0)

    d_n = boundary_matrix(K, n)
    r_n = matrix_rank(d_n) if d_n else 0

    d_np1 = boundary_matrix(K, n + 1)
    if d_np1:
        factors = smith_factors(d_np1)
        r_np1 = len(factors)
        torsion = [d for d in factors if d > 1]
    else:
        r_np1 = 0
        torsion = []

    betti = k_n - r_n - r_np1
    return HomologyGroup(dim=n, betti=betti, torsion=torsion)


def all_homology(K):
    """Compute H_n for all n from 0 to dimension of K."""
    return [homology(K, n) for n in range(K.dimension + 1)]


def euler_characteristic_from_homology(K):
    """χ(K) = Σ (-1)^n β_n. Should match K.euler_characteristic()."""
    groups = all_homology(K)
    return sum((-1)**g.dim * g.betti for g in groups)


def describe(K, name=None):
    """Print a readable homology summary for K."""
    label = name or repr(K)
    print(f"\n{'─' * 50}")
    print(f"  {label}")
    print(f"{'─' * 50}")
    print(f"  dim = {K.dimension}, χ = {K.euler_characteristic()}")
    for g in all_homology(K):
        marker = '  ' if g.is_trivial() else '→ '
        print(f"  {marker}H_{g.dim} = {g}")
    print()
