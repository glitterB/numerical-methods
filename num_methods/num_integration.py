def trapezoidal(f, a, b, n):
    """
    Compute integral of f(x) from a to b using the Trapezoidal Rule.

    Parameters
    ----------
    f : callable
        Function to integrate.
    a, b : float
        Integration limits.
    n : int
        Number of subintervals.

    Returns
    -------
    float
        Approximate integral value.
    """

    if n <= 0:
        raise ValueError("Number of subintervals must be positive.")

    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        s += f(a + i * h)

    return h * s
#-------------------------
def simpson_13(f, a, b, n):
    """
    Compute integral of f(x) from a to b using Simpson's 1/3 Rule.

    Parameters
    ----------
    f : callable
        Function to integrate.
    a, b : float
        Integration limits.
    n : int
        Number of subintervals (must be even).

    Returns
    -------
    float
        Approximate integral value.
    """

    if n <= 0 or n % 2 != 0:
        raise ValueError("n must be a positive even integer.")

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        weight = 4 if i % 2 != 0 else 2
        s += weight * f(a + i * h)

    return (h / 3) * s

#-------------------------
def simpson_38(f, a, b, n):
    """
    Compute integral of f(x) from a to b using Simpson's 3/8 Rule.

    Parameters
    ----------
    f : callable
        Function to integrate.
    a, b : float
        Integration limits.
    n : int
        Number of subintervals (must be multiple of 3).

    Returns
    -------
    float
        Approximate integral value.
    """

    if n <= 0 or n % 3 != 0:
        raise ValueError("n must be a positive integer multiple of 3.")

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        weight = 3 if i % 3 != 0 else 2
        s += weight * f(a + i * h)

    return (3 * h / 8) * s