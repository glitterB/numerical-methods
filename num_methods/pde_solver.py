def laplace_2d(nx, ny, bc, max_iter=500, tol=1e-6):
    """
    Solve 2D Laplace equation (elliptical) on a rectangular grid.
    
    Parameters
    ----------
    nx, ny : int
        Number of interior grid points.
    bc : dict
        Boundary conditions: {'top':..., 'bottom':..., 'left':..., 'right':...}
    max_iter : int
        Maximum number of iterations.
    tol : float
        Convergence tolerance.
    
    Returns
    -------
    T : np.ndarray
        2D solution array including boundaries.
    """
    # Initialize grid
    T = [[0.0 for _ in range(nx + 2)] for _ in range(ny + 2)]
    
    # Apply boundary conditions
    for i in range(nx + 2):
        T[0][i] = bc.get('top', 0.0)
        T[-1][i] = bc.get('bottom', 0.0)
    for j in range(ny + 2):
        T[j][0] = bc.get('left', 0.0)
        T[j][-1] = bc.get('right', 0.0)
    
    for _ in range(max_iter):
        T_old = [row[:] for row in T]
        max_diff = 0.0
        
        for j in range(1, ny + 1):
            for i in range(1, nx + 1):
                T[j][i] = 0.25 * (T_old[j-1][i] + T_old[j+1][i] +
                                   T_old[j][i-1] + T_old[j][i+1])
                max_diff = max(max_diff, abs(T[j][i] - T_old[j][i]))
        
        if max_diff < tol:
            break
    
    return T
#------------------------------------------
def heat_explicit(nx, nt, alpha, dx, dt, bc, initial):
    """
    Solve 1D heat equation (parabolic) using explicit finite difference.
    
    Parameters
    ----------
    nx : int
        Number of spatial points.
    nt : int
        Number of time steps.
    alpha : float
        Thermal diffusivity coefficient.
    dx : float
        Spatial step size.
    dt : float
        Time step size.
    bc : tuple
        Boundary conditions (left, right)
    initial : callable
        Initial condition function f(x)
    
    Returns
    -------
    T : np.ndarray
        Solution array of shape (nt+1, nx)
    """
    # Initialize solution grid
    T = [[0.0 for _ in range(nx)] for _ in range(nt + 1)]
    
    # Set initial condition
    for i in range(nx):
        T[0][i] = initial(i * dx)
    
    # Apply boundary conditions
    for n in range(nt + 1):
        T[n][0] = bc[0]
        T[n][-1] = bc[1]
    
    lam = alpha * dt / dx**2
    
    for n in range(nt):
        T_next = T[n][:]  # copy current row
        for i in range(1, nx - 1):
            T_next[i] = T[n][i] + lam * (T[n][i+1] - 2*T[n][i] + T[n][i-1])
        T[n+1] = T_next
    
    return T