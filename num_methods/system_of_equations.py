def _validate_system(A, b):
    n = len(b)
    if any(len(row) != n for row in A):
        raise ValueError("Matrix A must be square and compatible with b.")
#--------------------------
def gauss_elimination(A, b, pivoting=False):
    """
    Solve Ax = b using Gaussian elimination.

    Parameters
    ----------
    A : list of lists
        Coefficient matrix.
    b : list
        Right-hand side vector.
    pivoting : bool, optional
        Enable partial pivoting.

    Returns
    -------
    x : list
        Solution vector.

    Raises
    ------
    ValueError
        If system is singular or dimensions are invalid.
    ZeroDivisionError
        If zero pivot encountered and pivoting is disabled.
    """

    _validate_system(A, b)
    n = len(b)

    # Copy inputs to avoid mutation
    a = [row[:] for row in A]
    c = b[:]

    # Forward elimination
    for i in range(n):
        if pivoting:
            max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
            a[i], a[max_row] = a[max_row], a[i]
            c[i], c[max_row] = c[max_row], c[i]

        if a[i][i] == 0:
            raise ZeroDivisionError("Zero pivot encountered.")

        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            c[j] -= factor * c[i]

    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = c[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))
        x[i] = s / a[i][i]

    return x
#--------------------------
def gauss_seidel(
    A,
    b,
    x0=None,
    tol=1e-6,
    max_iter=100,
    return_history=False
):
    """
    Solve Ax = b using the Gauss–Seidel iterative method.

    Parameters
    ----------
    A : list of lists
        Coefficient matrix.
    b : list
        Right-hand side vector.
    x0 : list, optional
        Initial guess (defaults to zero vector).
    tol : float, optional
        Convergence tolerance.
    max_iter : int, optional
        Maximum number of iterations.
    return_history : bool, optional
        If True, return solution history.

    Returns
    -------
    x : list
        Solution vector.
    iterations : int
        Number of iterations performed.
    history : list (optional)
        Solution vectors per iteration.

    Raises
    ------
    ValueError
        If dimensions are invalid.
    RuntimeError
        If method fails to converge.
    """

    _validate_system(A, b)
    n = len(b)

    x = x0[:] if x0 is not None else [0.0] * n
    history = []

    for iteration in range(1, max_iter + 1):
        x_old = x[:]

        for i in range(n):
            s = b[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)
            if A[i][i] == 0:
                raise ZeroDivisionError("Zero diagonal element.")
            x[i] = s / A[i][i]

        history.append(x[:])

        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            if return_history:
                return x, iteration, history
            return x, iteration

    raise RuntimeError("Gauss–Seidel method did not converge.")

#--------------------------