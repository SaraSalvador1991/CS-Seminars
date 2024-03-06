import unittest
from Conic_Section_Class import Conic_Section
from get_shapeFunction import get_shape

class TestCircle(unittest.TestCase):
    def runTest(self):
        CS = Conic_Section(3,-1,1)
        self.assertEqual(get_shape(CS), "This is an elipse!", "something is wrong")
# run the test
if __name__ == '__main__':
    unittest.main()