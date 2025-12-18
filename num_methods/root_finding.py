def bisection(
    f,
    a,
    b,
    tol=1e-6,
    max_iter=100,
    return_history=False
):
    """
    Find a root of f(x) = 0 using the Bisection Method.

    Parameters
    ----------
    f : callable
        Function for which the root is sought.
    a, b : float
        Interval endpoints such that f(a)*f(b) < 0.
    tol : float, optional
        Convergence tolerance on |f(x)|.
    max_iter : int, optional
        Maximum number of iterations.
    return_history : bool, optional
        If True, return list of midpoints.

    Returns
    -------
    root : float
        Estimated root.
    iterations : int
        Number of iterations performed.
    history : list (optional)
        Midpoint values per iteration.

    Raises
    ------
    ValueError
        If f(a) and f(b) do not bracket a root.
    RuntimeError
        If method fails to converge.
    """

    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    history = []

    for iteration in range(1, max_iter + 1):
        c = 0.5 * (a + b)
        fc = f(c)

        history.append(c)

        if abs(fc) < tol:
            if return_history:
                return c, iteration, history
            return c, iteration

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise RuntimeError("Bisection method did not converge.")
#-------------------------------
def regula_falsi(
    f,
    a,
    b,
    tol=1e-6,
    max_iter=100,
    return_history=False
):
    """
    Find a root of f(x) = 0 using the Regula Falsi (False Position) method.

    Parameters
    ----------
    f : callable
        Function for which the root is sought.
    a, b : float
        Interval endpoints such that f(a)*f(b) < 0.
    tol : float, optional
        Convergence tolerance on |f(x)|.
    max_iter : int, optional
        Maximum number of iterations.
    return_history : bool, optional
        If True, return list of intermediate root estimates.

    Returns
    -------
    root : float
        Estimated root.
    iterations : int
        Number of iterations performed.
    history : list (optional)
        Root estimates per iteration.

    Raises
    ------
    ValueError
        If f(a) and f(b) do not bracket a root.
    RuntimeError
        If method fails to converge.
    """

    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    history = []

    for iteration in range(1, max_iter + 1):
        # False position formula
        c = a - fa * (a - b) / (fa - fb)
        fc = f(c)

        history.append(c)

        if abs(fc) < tol:
            if return_history:
                return c, iteration, history
            return c, iteration

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise RuntimeError("Regula Falsi method did not converge.")
#-------------------------------
def newton_raphson(
    f,
    df,
    x0,
    tol=1e-6,
    max_iter=100,
    return_history=False
):
    """
    Find a root of f(x) = 0 using the Newton–Raphson method.

    Parameters
    ----------
    f : callable
        Function for which the root is sought.
    df : callable
        Derivative of f.
    x0 : float
        Initial guess.
    tol : float, optional
        Convergence tolerance on |f(x)|.
    max_iter : int, optional
        Maximum number of iterations.
    return_history : bool, optional
        If True, return list of iterates.

    Returns
    -------
    root : float
        Estimated root.
    iterations : int
        Number of iterations performed.
    history : list (optional)
        Iterative estimates.

    Raises
    ------
    ZeroDivisionError
        If derivative becomes zero.
    RuntimeError
        If method fails to converge.
    """

    x = x0
    history = []

    for iteration in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ZeroDivisionError("Derivative became zero during iteration.")

        x_new = x - fx / dfx
        history.append(x_new)

        if abs(f(x_new)) < tol:
            if return_history:
                return x_new, iteration, history
            return x_new, iteration

        x = x_new

    raise RuntimeError("Newton–Raphson method did not converge.")
