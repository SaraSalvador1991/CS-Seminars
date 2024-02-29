# Unit tests written by AI Assistant.

import unittest
from classes.node import Node


class TestNode(unittest.TestCase):

    def test_node_init(self):
        node = Node(5)
        self.assertEqual(node.get_data(), 5)
        self.assertIsNone(node.get_next())

        # Testing when node is initialized without any data
        node = Node()
        self.assertIsNone(node.get_data())
        self.assertIsNone(node.get_next())

    def test_get_data(self):
        node = Node("Test")
        self.assertEqual(node.get_data(), "Test")

    def test_get_next(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.set_next(node2)
        self.assertEqual(node1.get_next(), node2)

    def test_set_next(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.set_next(node2)
        self.assertEqual(node1.get_next(), node2)

        # Testing set_next with None
        node1.set_next(None)
        self.assertIsNone(node1.get_next())

        # Testing set_next with non-Node object
        with self.assertRaises(TypeError):
            node1.set_next("Not a Node Object")


if __name__ == '__main__':
    unittest.main()
