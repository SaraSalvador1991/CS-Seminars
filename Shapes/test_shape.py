import unittest
from Conic_Section_Class import Conic_Section
from Functions_shape import get_shape
from Functions_shape import extract_poly_coeff
from sympy import symbols, Poly

class TestCircle(unittest.TestCase):
    def runTest(self):
        x, y = symbols('x y')
        f =  3*x**2 + 5*x*y + y**2 + 3*x + 7*y + 1   # Example polynomial of a conic section
        coefficients = extract_poly_coeff(f)
        A = coefficients[5]
        B = coefficients[4]
        C = coefficients[2]
        CS = Conic_Section(A,B,C)
        self.assertEqual(get_shape(CS), "This is a hyperbola!", "something is wrong")
# run the test
if __name__ == '__main__':
    unittest.main()