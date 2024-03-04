import numpy as np

class Torus:
    def __init__(self, R, r, nu, nv):
        self.R = float(R)
        self.r = float(r)
        self.nu = float(nu)
        self.nv = float(nv)

        u = np.linspace(0, 2.*np.pi, self.nu)
        v = np.linspace(0, 2.*np.pi, self.nv)
        self.u, self.v = np.meshgrid(u,v)
    def get_Area(self):

        return 4*np.pi**2*self.R*self.r

    def get_Volume(self):
        return  2*np.pi**2*self.R*self.r**2


    def get_xyz(self):
        x = (self.R+self.r * np.cos(self.u))*np.cos(self.v)
        y = (self.R+self.r * np.cos(self.u))*np.sin(self.v)
        z = self.r * np.sin(self.u)




