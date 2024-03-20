import unittest
from classes.binary_tree import BinaryTree


class BinaryTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    def test_insert(self):
        # Assuming an empty tree initially
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.assertEqual(self.tree.get_size(), 3)

        # Test inserting a key that already exists.
        with self.assertRaises(ValueError):
            self.tree.insert(10)

    def test_find(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(5)
        self.assertTrue(self.tree.find(10))
        self.assertFalse(self.tree.find(15))
        self.assertFalse(self.tree.find(30))
        self.assertTrue(self.tree.find(5))

    def test_delete(self):
        # Test deleting a node that does not exist.
        with self.assertRaises(ValueError):
            self.tree.delete(10)

        # Test deleting a node with no children.
        self.tree.insert(10)
        self.tree.delete(10)
        self.assertFalse(self.tree.find(10))
        self.assertEqual(self.tree.get_size(), 0)
        self.assertEqual(self.tree.get_height(), 0)

        # Test deleting a node with one child.
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.delete(10)
        self.assertFalse(self.tree.find(10))
        self.assertTrue(self.tree.find(5))
        self.assertEqual(self.tree.get_size(), 1)

        # Reset tree.
        self.tree.burn_off()

        # Test deleting a node with two children.
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(20)
        self.tree.delete(10)
        self.assertFalse(self.tree.find(10))
        self.assertTrue(self.tree.find(5))
        self.assertTrue(self.tree.find(20))
        self.assertEqual(self.tree.get_size(), 2)

    def test_get_size(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.delete(10)
        self.assertEqual(self.tree.get_size(), 2)
        self.tree.delete(20)
        self.tree.delete(30)
        self.assertEqual(self.tree.get_size(), 0)

    def test_get_height(self):
        self.assertEqual(self.tree.get_height(), 0)
        self.tree.insert(10)
        self.assertEqual(self.tree.get_height(), 1)
        self.tree.insert(20)
        self.tree.insert(25)
        self.tree.insert(15)
        self.tree.insert(30)
        self.assertEqual(self.tree.get_height(), 4)
        self.tree.insert(5)
        self.assertEqual(self.tree.get_height(), 4)

    def test_burn_off(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.burn_off()
        self.assertEqual(self.tree.get_size(), 0)
        self.assertEqual(self.tree.get_height(), 0)
        self.assertFalse(self.tree.find(10))
        self.assertFalse(self.tree.find(20))
        self.assertFalse(self.tree.find(30))


if __name__ == "__main__":
    unittest.main()


