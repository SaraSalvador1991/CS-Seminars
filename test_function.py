
import unittest
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")


# run the test
if __name__ == '__main__':
    unittest.main()


class Even:
    def __init__(self,x):
        self.x = x
    def is_even(self):
        if self.x % 2 == 0:
            return "True"
import unittest

class TestEven(unittest.TestCase):
    def test_even(self):
        even = Even(2)
        self.assertEqual(even.is_even(), 'True', 'function is wrong.')

if __name__ == '__main__':
    unittest.main()
# -------------

class Prime:
    def __init__(self,x):
        self.x = x

    def is_prime(self):
        if self.x == 1:
            return "False"
        elif self.x > 1:
            for i in range(2, self.x):
                if (self.x % i) == 0:
                    return "False"
            else:
                return "True"

import unittest
class TestPrime(unittest.TestCase):
    def test_prime(self):
        prime = Prime(10)
        self.assertEqual(prime.is_prime(), "True", "function is wrong.")

if __name__ == '__main__':
    unittest.main()

# -----------------

class Hypotenuse:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
    def get_hypotenuse(self):
        return (self.c1**2+self.c2**2)**0.5

import unittest
class TestPrime(unittest.TestCase):
    def test_hypotenuse(self):
        hypotenuse = Hypotenuse(3,4)
        self.assertEqual(hypotenuse.get_hypotenuse(), 5, "function is wrong.")

if __name__ == '__main__':
    unittest.main()