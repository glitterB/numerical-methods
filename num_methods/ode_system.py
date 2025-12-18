def euler_system(F, x0, y0, xn, n, return_history=False):
    """
    Solve a system of first-order ODEs using Euler's method.

    Parameters
    ----------
    F : callable
        Function F(x, y) returning list of derivatives.
    x0 : float
        Initial x.
    y0 : list
        Initial state vector.
    xn : float
        Final x.
    n : int
        Number of steps.
    """

    h = (xn - x0) / n
    x = x0
    y = y0[:]
    history = [(x, y[:])]

    for _ in range(n):
        dy = F(x, y)
        y = [y[i] + h * dy[i] for i in range(len(y))]
        x += h
        history.append((x, y[:]))

    if return_history:
        return y, history
    return y
#--------------------
def rk2_system(F, x0, y0, xn, n, return_history=False):
    """
    Solve a system of first-order ODEs using RK2.
    """

    h = (xn - x0) / n
    x = x0
    y = y0[:]
    history = [(x, y[:])]

    for _ in range(n):
        k1 = F(x, y)
        y_temp = [y[i] + h * k1[i] for i in range(len(y))]
        k2 = F(x + h, y_temp)

        y = [
            y[i] + 0.5 * h * (k1[i] + k2[i])
            for i in range(len(y))
        ]

        x += h
        history.append((x, y[:]))

    if return_history:
        return y, history
    return y
#-----------------