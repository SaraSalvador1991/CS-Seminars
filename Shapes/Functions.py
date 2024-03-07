'''
from Conic_Section_Class import Conic_Section
def get_shape(CS:Conic_Section):
    Delta = CS.B ** 2 - 4 * CS.A * CS.C
    if Delta < 0 and CS.A != CS.C and CS.B != 0:
        return f"This is an elipse!"
    if Delta < 0 and CS.A == CS.C and CS.B == 0:
        return f"This is a circle!"
    if Delta == 0:
        return f"This is a parabola!"
    if Delta > 0 and CS.A + CS.C != 0:
        return f"This is a hyperbola!"
    if Delta > 0 and CS.A + CS.C == 0:
        return f"This is a rectangular hyperbola!"
'''

import sympy
import numpy

import sympy as sp

from sympy.abc import x, y
x,y,xy=sp.symbols('x,y,xy')
expression = x**2 + 5*xy + 5
c = [expression.coeff(x**2), expression.coeff(xy), expression.coeff(1)]
print(c)
print(sp.Poly(x**2+5*x*y+5,x,y, domain = 'ZZ').all_coeffs())