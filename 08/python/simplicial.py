"""
Simplicial complexes — the combinatorial heart of the computation.

A simplicial complex is a collection of simplices closed under taking faces.
Simplices are represented as sorted tuples of integer vertex labels.
"""

from itertools import combinations


class SimplicialComplex:
    """
    A simplicial complex built from a collection of generators.

    Automatically closes downward: if you give it a triangle (0,1,2),
    it includes all faces (0,1), (0,2), (1,2), (0,), (1,), (2,).

    Usage:
        K = SimplicialComplex([(0,1,2), (1,2,3)])
        K.simplices(1)      # all edges
        K.dimension         # highest dimension present
        K.euler_characteristic()
    """

    def __init__(self, generators):
        self._simplices = set()
        for s in generators:
            self._close(tuple(sorted(s)))

    def _close(self, s):
        """Add simplex s and all its faces."""
        if s in self._simplices:
            return
        self._simplices.add(s)
        for i in range(len(s)):
            face = s[:i] + s[i+1:]
            if face:
                self._close(face)

    def simplices(self, dim=None):
        """All simplices, optionally filtered by dimension."""
        if dim is None:
            return sorted(self._simplices, key=lambda s: (len(s), s))
        return sorted(s for s in self._simplices if len(s) == dim + 1)

    @property
    def dimension(self):
        return max(len(s) - 1 for s in self._simplices)

    @property
    def vertices(self):
        return self.simplices(0)

    def euler_characteristic(self):
        total = 0
        for s in self._simplices:
            dim = len(s) - 1
            total += (-1) ** dim
        return total

    def betti_numbers(self):
        """Compute all Betti numbers. Returns list [β_0, β_1, ..., β_d]."""
        from homology import all_homology
        groups = all_homology(self)
        return [g.betti for g in groups]

    def __repr__(self):
        by_dim = {}
        for s in self._simplices:
            d = len(s) - 1
            by_dim.setdefault(d, []).append(s)
        parts = []
        for d in sorted(by_dim):
            name = {0: 'vertices', 1: 'edges', 2: 'triangles'}.get(d, f'{d}-simplices')
            parts.append(f"{len(by_dim[d])} {name}")
        return f"SimplicialComplex({', '.join(parts)})"
