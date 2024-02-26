from typing import Any


class Node(object):
    """
    A class representing a node in a linked list.
    """

    def __init__(self, data=None):
        self.__prev = None
        self.__next = None
        self.__data = data

    def get_data(self) -> Any:
        return self.__data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_next(self, next_node):
        # Check if the object is an instance of Node
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node instance or None.")
        self.__next = next_node

    def set_prev(self,prev_node):
        # Check if the object is an instance of Node
        if not isinstance(prev_node, Node) and prev_node is not None:
            raise TypeError("prev_node must be a Node instance or None.")
        self.__prev = prev_node
