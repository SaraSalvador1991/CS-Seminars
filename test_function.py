import unittest
'''
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
'''

class Prime:
    def __init__(self):
        int self
    def is_prime(self):
        if self%2 ==0:
            return 'True'

import unittest

class TestCalculations(unittest.TestCase):

    def test_prime(self):
        prime = Prime(3)
        self.assertEqual(prime.is_prime(), 'True', 'function is wrong.')

if __name__ == '__main__':
    unittest.main()

