
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq
from sympy.plotting import plot_implicit

def plot_conic_section(expression):
    """
    Plot a conic section given its expression.

    Arguments:
    expression: SymPy expression representing the conic section equation.
    """
    # Define symbols
    x, y = symbols('x y')

    # Plot the conic section
    p1 = plot_implicit(Eq(expression, 0), (x, -10, 10), (y, -10, 10), show=False)

    # Set plot parameters
    p1.xlabel = 'x'
    p1.ylabel = 'y'
    p1.title = 'Conic Section Plot'
    p1.show()

# Example usage:
x, y = symbols('x y')
expression = x**2 + 3*x*y + y**2 + 7*x+ 9*y - 9  # Example expression of a circle with radius 3
plot_conic_section(expression)
