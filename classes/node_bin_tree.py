from __future__ import annotations
from typing import Any, Optional


class Node(object):
    """
    A class representing a node in a binary tree where integers are stored.
    """

    def __init__(self, key: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.__key = key  # value of the node
        self.__left = left  # left child
        self.__right = right  # right child

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int) -> None:
        self.__key = key

    def get_left(self) -> Optional[Node]:
        return self.__left

    def get_right(self) -> Optional[Node]:
        return self.__right

    def set_left(self, left: Optional[Node]) -> None:
        # Check if the object is an instance of Node or is None
        if not isinstance(left, Node) and left is not None:
            raise TypeError("'left' must be a Node instance or None.")
        self.__left = left
        
    def set_right(self, right: Optional[Node]) -> None:
        # Check if the object is an instance of Node or is None
        if not isinstance(right, Node) and right is not None:
            raise TypeError("'right' must be a Node instance or None.")
        self.__right = right
