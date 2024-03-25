import unittest
import numpy as np
#from Circle_Class import Circle
from Functions_Circle import compute_intersection
from Functions_Circle import Area
from inheritance_Circle_Square import Point
from inheritance_Circle_Square import Shape
from inheritance_Circle_Square import Circle
from inheritance_Circle_Square import Square
from inheritance_Circle_Square import Triangle
#from Functions_Circle import Circumference
class TestCircle(unittest.TestCase):
    '''
    def test_constructor(self):
        c1 = Circle(1,0,0)
        c2 = Circle(2,2,-1)
        self.assertEqual(compute_intersection(c1,c2), "The two circles intersect in two points", "something is wrong")
        self.assertEqual(Area(c1), 3.142,  "something is wrong")
        self.assertEqual(Circumference(c2), 12.566, "something is wrong")
    '''
    def test_radius(self):
        circle = Circle(Point(0, 0), 5)
       # check if the radius is positive
        #self.assertTrue(circle.r > 0, "Il raggio del cerchio non è positivo")
       # self.assertEqual(circle.r,5 , "Il raggio del cerchio non è 5")
    '''
    def test_circumference(self):
        c1 = Circle(1, 0, 0)
        self.assertAlmostEqual(c1.circumference(), 2*3.14, 2, "not right" )
        
    '''
    def test_inheritance(self):
        items = [Circle((1,1), 3), Square((1,1), 5), Triangle((1,1), 5, 3)]
        self.assertEqual(len(items), 3)
        result = 0
        for item in items:
            result = result + item.area()
        print(result)

    def test_weight(self):
        circle = Circle(Point(0, 0), 5)
        circle.set_weight(5)
        self.assertEqual(circle.weight, 5)
# run the test
if __name__ == '__main__':
    unittest.main()

