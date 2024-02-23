from typing import Any


class Node(object):
    """
    A class representing a node in a linked list.
    """

    def __init__(self, data=None):
        self.__next = None
        self.__data = data

    def get_data(self) -> Any:
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        # Check if the object is an instance of Node
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node instance or None.")
        self.__next = next_node


if __name__ == '__main__':
    root = Node(11)
    new_node = Node('bliblablup')
    root.set_next(new_node)
    print(root.get_data())
    try:
        print(root.__data)
    except AttributeError:
        print("An AttributeError was raised as expected.")
    print(new_node.get_data())
    print(root.get_next().get_data())
    print(root.get_next())
    print(new_node.get_next())
    try:
        root.set_next('node')
    except TypeError:
        print("An TypeError was raised as expected.")
