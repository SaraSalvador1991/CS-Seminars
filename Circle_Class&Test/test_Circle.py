import unittest
import numpy as np
from Circle_Class import Circle
from Functions_Circle import compute_intersection
from Functions_Circle import Area
from Functions_Circle import Circumference
class TestCircle(unittest.TestCase):
    def runTest(self):
        c1 = Circle(1,0,0)
        c2 = Circle(2,2,-1)
        self.assertEqual(compute_intersection(c1,c2), "The two circles intersect in two points", "something is wrong")
        self.assertEqual(Area(c1), 3.142,  "something is wrong")
        self.assertEqual(Circumference(c2), 12.566, "something is wrong")
# run the test
if __name__ == '__main__':
    unittest.main()
