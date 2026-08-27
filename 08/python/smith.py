"""
Smith Normal Form over the integers.

Given an integer matrix M, the Smith normal form is a diagonal matrix D
with d_1 | d_2 | ... | d_r (the invariant factors), achievable by
integer row and column operations (add multiples of rows/cols, swap, negate).

We only need the invariant factors — the actual transformation matrices U, V
such that D = UMV are not computed here.

The algorithm is a generalization of Gaussian elimination using the
Euclidean algorithm instead of exact division.

Reference: Henri Cohen, "A Course in Computational Algebraic Number Theory",
           Algorithm 2.4.14.
"""


def smith_factors(M):
    """
    Compute the nonzero invariant factors of integer matrix M.

    Returns a list [d_1, d_2, ..., d_r] of positive integers where each
    divides the next. The rank of M is r.

    These factors determine the homology:
        H_n = Z^β ⊕ Z/d_1Z ⊕ ... ⊕ Z/d_kZ
    where the d_i > 1 are torsion coefficients.
    """
    if not M or not M[0]:
        return []

    A = [list(row) for row in M]
    nrows, ncols = len(A), len(A[0])
    factors = []
    start = 0

    while start < nrows and start < ncols:
        pivot = _find_min_nonzero(A, start, nrows, ncols)
        if pivot is None:
            break

        _swap_rows(A, start, pivot[0])
        _swap_cols(A, start, pivot[1])

        while True:
            _eliminate_col(A, start, nrows, ncols)
            _eliminate_row(A, start, nrows, ncols)

            bad = _find_nondivisible(A, start, nrows, ncols)
            if bad is None:
                break
            # Adding a row with a non-divisible entry makes A[start][start]
            # smaller via the Euclidean algorithm on the next iteration.
            for j in range(ncols):
                A[start][j] += A[bad[0]][j]

        if A[start][start] < 0:
            for j in range(ncols):
                A[start][j] = -A[start][j]

        factors.append(A[start][start])
        start += 1

    return factors


def rank(M):
    """Rank of integer matrix M (number of nonzero invariant factors)."""
    return len(smith_factors(M))


def _find_min_nonzero(A, start, nrows, ncols):
    best = None
    for i in range(start, nrows):
        for j in range(start, ncols):
            if A[i][j] != 0:
                if best is None or abs(A[i][j]) < abs(A[best[0]][best[1]]):
                    best = (i, j)
    return best


def _swap_rows(A, i, j):
    A[i], A[j] = A[j], A[i]


def _swap_cols(A, i, j):
    for row in A:
        row[i], row[j] = row[j], row[i]


def _eliminate_col(A, start, nrows, ncols):
    """Use row `start` to zero out column `start` for all rows below start."""
    changed = True
    while changed:
        changed = False
        for i in range(start + 1, nrows):
            if A[i][start] == 0:
                continue
            if abs(A[i][start]) < abs(A[start][start]):
                _swap_rows(A, start, i)
            q = A[i][start] // A[start][start]
            for j in range(ncols):
                A[i][j] -= q * A[start][j]
            if A[i][start] != 0:
                changed = True


def _eliminate_row(A, start, nrows, ncols):
    """Use col `start` to zero out row `start` for all cols right of start."""
    changed = True
    while changed:
        changed = False
        for j in range(start + 1, ncols):
            if A[start][j] == 0:
                continue
            if abs(A[start][j]) < abs(A[start][start]):
                _swap_cols(A, start, j)
            q = A[start][j] // A[start][start]
            for i in range(nrows):
                A[i][j] -= q * A[i][start]
            if A[start][j] != 0:
                changed = True


def _find_nondivisible(A, start, nrows, ncols):
    """Find an entry in A[start+1:, start+1:] not divisible by A[start][start]."""
    p = A[start][start]
    for i in range(start + 1, nrows):
        for j in range(start + 1, ncols):
            if A[i][j] % p != 0:
                return (i, j)
    return None
