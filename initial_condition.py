import numpy as np


class InitialCondition(): 
    
    def __init__(self, w=10, h=10, dx=0.1, dy=0.1, T=100): 
        self.w = int(w)
        self.h = int(h)
        self.dx = dx
        self.dy = dy
        self.Nx = int(self.w/self.dx)
        self.Ny = int(self.h/self.dy)
        self.T = T
        self.u0 = 0 * np.ones((self.Nx, self.Ny))

    def border(self, t=1): 
        self.u0[0:t, :] = self.T

    def rectangle(self, cx=20, cy=20, tx=1, ty=1): 
        self.u0[cx:cx + tx, cy:cy + ty] = self.T

    def circle(self, cx=5, cy=5, r=1): 
        for i in range(self.Nx):
            for j in range(self.Ny):
                p2 = (i*self.dx - cx)**2 + (j*self.dy - cy)**2
                if p2 < r ** 2:
                    self.u0[i,j] = self.T