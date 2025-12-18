def euler(f, x0, y0, xn, n, return_history=False):
    """
    Solve dy/dx = f(x, y) using the Euler method.

    Parameters
    ----------
    f : callable
        Right-hand side function f(x, y).
    x0, y0 : float
        Initial condition.
    xn : float
        Final x value.
    n : int
        Number of steps.
    return_history : bool, optional
        If True, return solution history.

    Returns
    -------
    y : float
        Solution at x = xn.
    history : list (optional)
        List of (x, y) pairs.
    """

    if n <= 0:
        raise ValueError("Number of steps must be positive.")

    h = (xn - x0) / n
    x, y = x0, y0
    history = [(x, y)]

    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h
        history.append((x, y))

    if return_history:
        return y, history
    return y
#---------------------------
def rk2(f, x0, y0, xn, n, return_history=False):
    """
    Solve dy/dx = f(x, y) using 2nd-order Runge–Kutta (RK2).

    Parameters
    ----------
    f : callable
        Right-hand side function f(x, y).
    x0, y0 : float
        Initial condition.
    xn : float
        Final x value.
    n : int
        Number of steps.
    return_history : bool, optional
        If True, return solution history.

    Returns
    -------
    y : float
        Solution at x = xn.
    history : list (optional)
        List of (x, y) pairs.
    """

    if n <= 0:
        raise ValueError("Number of steps must be positive.")

    h = (xn - x0) / n
    x, y = x0, y0
    history = [(x, y)]

    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y = y + 0.5 * (k1 + k2)
        x = x + h
        history.append((x, y))

    if return_history:
        return y, history
    return y

#--------------------------
def rk4(f, x0, y0, xn, n, return_history=False):
    """
    Solve dy/dx = f(x, y) using 4th-order Runge–Kutta (RK4).

    Parameters
    ----------
    f : callable
        Right-hand side function f(x, y).
    x0, y0 : float
        Initial condition.
    xn : float
        Final x value.
    n : int
        Number of steps.
    return_history : bool, optional
        If True, return solution history.

    Returns
    -------
    y : float
        Solution at x = xn.
    history : list (optional)
        List of (x, y) pairs.
    """

    if n <= 0:
        raise ValueError("Number of steps must be positive.")

    h = (xn - x0) / n
    x, y = x0, y0
    history = [(x, y)]

    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        history.append((x, y))

    if return_history:
        return y, history
    return y