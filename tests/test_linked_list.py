# Unit tests written by AI Assistant.

import unittest
from classes.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_get_size(self):
        self.assertEqual(self.ll.get_size(), 0)

        self.ll.append(1)
        self.assertEqual(self.ll.get_size(), 1)

    def test_append(self):
        self.ll.append(5)
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll.get_data_at_index(0), 5)

        # test appending with multiple elements
        self.ll = LinkedList()  # reset the LinkedList
        elements = range(1000)
        for i in elements:
            self.ll.append(i)
            self.assertEqual(self.ll.get_data_at_index(i), i)
        self.assertEqual(self.ll.get_size(), len(elements))

    def test_insert(self):
        self.ll.insert(5, 0)
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll.get_data_at_index(0), 5)

        # test inserting at various positions
        self.ll.insert(6, 1)
        self.assertEqual(self.ll.get_data_at_index(1), 6)
        self.ll.insert(7, 1)
        self.assertEqual(self.ll.get_data_at_index(1), 7)
        self.assertEqual(self.ll.get_data_at_index(2), 6)

    def test_remove_data(self):
        self.ll.append(5)
        self.ll.append(5)
        self.ll.remove_data(5)
        self.assertEqual(self.ll.get_size(), 1)
        # test removing an element that does not exist
        with self.assertRaises(ValueError):
            self.ll.remove_data(10)

    def test_remove_index(self):
        self.ll.append(5)
        self.ll.remove_index(0)
        self.assertEqual(self.ll.get_size(), 0)
        self.assertEqual(self.ll.head, None)
        # test removing an index that does not exist
        with self.assertRaises(IndexError):
            self.ll.remove_index(10)

    def test_get_data_at_index(self):
        self.ll.append(5)
        self.assertEqual(self.ll.get_data_at_index(0), 5)
        # test getting data at an index that does not exist
        with self.assertRaises(IndexError):
            self.ll.get_data_at_index(10)


if __name__ == '__main__':
    unittest.main()
