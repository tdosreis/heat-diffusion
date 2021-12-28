import numpy as np


def timesteps(u0, nsteps=1000): 
    
    def _solver(u0, u, dx=0.1, dy=0.1, D=4.0):
        dx2 = dx * dx
        dy2 = dy * dy
        dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
        uxx = (u0[2:, 1:-1] - 2*u0[1:-1, 1:-1] + u0[:-2, 1:-1])/dx2
        uyy = (u0[1:-1, 2:] - 2*u0[1:-1, 1:-1] + u0[1:-1, :-2])/dy2
        u[1:-1, 1:-1] = u0[1:-1, 1:-1] + D * dt * (uxx + uyy)
        u0 = u.copy()
        return u0, u, dt
    
    u = u0.copy()
    for m in range(nsteps):
        u0, u, dt = _solver(u0, u)
        
    return u0, u, dt