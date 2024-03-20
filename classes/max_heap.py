from typing import List


class MaxHeap:
    def __init__(self):
        self.__heap: List[int] = []
        self.__size: int = 0

    def get_size(self) -> int:
        """
        Get the number of elements in the Max-Heap.

        :return: The size.
        """
        return self.__size

    def get_heap(self) -> List[int]:
        """
        Return the Max-Heap as a list of integers.

        :return: A list containing the elements in the Max-Heap.
        """
        return self.__heap

    def insert(self, key: int) -> None:
        """
        Inserts the specified key into the Max-Heap.

        :param key: The key to be inserted.
        :return: None
        """
        pass

    def remove(self, index: int) -> None:
        """
        Removes an element at the specified index.

        :param index: The index of the element to be removed.
        :return: None
        """
        pass

    def pop(self, index: int) -> int:
        """
        Removes the element at the given index and returns its key.

        :param index: The index of the element to be removed.
        :return: The key of the removed element.
        """
        pass

    def get_max(self) -> int | None:
        """
        Returns the maximum element of the Max-Heap.

        :return: The maximum element of the Max-Heap, or None if the Max-Heap is empty.
        :raises IndexError: If the Max-Heap is empty.
        """
        if self.get_size() == 0:
            raise IndexError("Max-Heap is empty.")
        return self.get_heap()[0]

    def find_all(self, key: int) -> List[int]:
        """
        Finds all occurrences of the given key in the Max-Heap.

        :param key: The key to search for.
        :return: A list of indices of all occurrences of the key.
        """
        pass
    