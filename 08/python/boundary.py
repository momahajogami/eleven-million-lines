"""
Boundary maps for simplicial complexes.

The boundary of an oriented n-simplex [v_0, v_1, ..., v_n] is the
alternating sum of its (n-1)-dimensional faces:

    ∂[v_0, ..., v_n] = Σ_{l=0}^{n} (-1)^l [v_0, ..., v̂_l, ..., v_n]

where v̂_l means v_l is omitted.

The boundary map ∂_n: C_n → C_{n-1} is represented as a matrix where:
  - rows are indexed by (n-1)-simplices
  - columns are indexed by n-simplices
  - entry (i, j) is the coefficient of the i-th (n-1)-simplex
    in the boundary of the j-th n-simplex

Key property: ∂_{n-1} ∘ ∂_n = 0 (the boundary of a boundary is zero).
This is what makes homology possible.
"""


def boundary_matrix(K, n):
    """
    Compute the boundary matrix ∂_n for simplicial complex K.

    Returns a 2D list (matrix) of integers with shape:
        len(K.simplices(n-1)) rows × len(K.simplices(n)) cols

    Returns [] if n == 0 or if there are no n-simplices.
    """
    if n == 0:
        return []

    n_simplices = K.simplices(n)
    nm1_simplices = K.simplices(n - 1)

    if not n_simplices or not nm1_simplices:
        return []

    idx = {s: i for i, s in enumerate(nm1_simplices)}
    nrows = len(nm1_simplices)
    ncols = len(n_simplices)
    M = [[0] * ncols for _ in range(nrows)]

    for j, sigma in enumerate(n_simplices):
        for l in range(len(sigma)):
            face = sigma[:l] + sigma[l+1:]
            sign = (-1) ** l
            M[idx[face]][j] = sign

    return M


def verify_boundary_squared_zero(K):
    """
    Check that ∂_{n-1} ∘ ∂_n = 0 for all n.
    Returns True if the identity holds everywhere.

    This is a sanity check — if it fails, something is wrong with the
    complex or the boundary computation.
    """
    for n in range(1, K.dimension + 1):
        d_n = boundary_matrix(K, n)
        d_nm1 = boundary_matrix(K, n - 1)
        if not d_n or not d_nm1:
            continue
        product = _matmul(d_nm1, d_n)
        if any(product[i][j] != 0
               for i in range(len(product))
               for j in range(len(product[0]))):
            return False
    return True


def _matmul(A, B):
    """Integer matrix multiplication."""
    m, k = len(A), len(A[0])
    n = len(B[0])
    C = [[0] * n for _ in range(m)]
    for i in range(m):
        for p in range(k):
            if A[i][p] == 0:
                continue
            for j in range(n):
                C[i][j] += A[i][p] * B[p][j]
    return C
