import unittest
import numpy as np
from Circle_Class import Circle
from Functions_Circle import compute_intersection
from Functions_Circle import Area
from Functions_Circle import Circumference
class TestCircle(unittest.TestCase):
    def runTest(self):
        c1 = Circle(0.5,1,1)
        c2 = Circle(1,3,3)
        self.assertEqual(compute_intersection(c1,c2), "The two circles do not intersect", "something is wrong")
        self.assertEqual(Area(c1), 0.785,  "something is wrong")
        self.assertEqual(Circumference(c2), 6.283, "something is wrong")
# run the test
if __name__ == '__main__':
    unittest.main()
