import unittest
import numpy as np
from Circle_Class import Circle
from Functions import compute_intersection
from Functions import Area
from Functions import Circumference
class TestCircle(unittest.TestCase):
    def runTest(self):
        c1 = Circle(0.5,1,1)
        c2 = Circle(1,3,3)
        self.assertEqual(compute_intersection(c1,c2), "The two circles do not intersect", "something is wrong")
        self.assertEqual(Area(c1), round(np.pi*0.5**2,3), "something is wrong")
        self.assertEqual(Circumference(c2), round(np.pi * 1* 2, 3), "something is wrong")
# run the test
if __name__ == '__main__':
    unittest.main()
