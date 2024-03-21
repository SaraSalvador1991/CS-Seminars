from typing import List


class MaxHeap:
    """
    A MaxHeap class represents a binary max-heap data structure.
    This is a heap implementation without nodes. The tree is just a list.

    First index in the max-heap is 0 (root).
    Parent has index i, then:
        The index of the left child is 2*i+1
        The index of the right child is 2*i+2
    The parent's index of a child with index i is (i-1)\\2

    It supports the following operations:
    - Getting the size of the heap (number of elements)
    - Getting the heap
    - Inserting an element into the heap
    - Removing an element from the heap
    - Removing and returning an element from the heap
    - Retrieving the maximum element from the heap
    - Searching for occurrences of a given key in the heap
    """
    def __init__(self):
        self.__heap: List[int] = []
        self.__size: int = 0

    # region public methods
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
        self.__heap.append(key)
        self.__size += 1
        if self.__size > 1:
            self._heapify_up(key, self.__size - 1)

    def remove(self, index: int) -> None:
        """
        Removes an element at the specified index.

        :param index: The index of the element to be removed.
        :return: None
        """
        # if self.__size == 0:
        #     raise IndexError("Max-Heap is empty.")
        # if index < 0 or index >= self.__size:
        #     raise IndexError("Invalid index.")
        self._check_index(index)
        self.__heap[index] = self.__heap[self.__size - 1]
        del self.__heap[self.__size - 1]
        self.__size -= 1
        if index == self.__size:
            return
        parent_index = (index - 1) // 2
        if self.__heap[index] > self.__heap[parent_index]:
            self._heapify_up(self.__heap[index], index)
        else:
            self._heapify_down(self.__heap[index], index)

    def pop(self, index: int) -> int:
        """
        Removes the element at the given index and returns its key.

        :param index: The index of the element to be removed.
        :return: The key of the removed element.
        """
        # if self.__size == 0:
        #     raise IndexError("Max-Heap is empty.")
        # if index < 0 or index >= self.__size:
        #     raise IndexError("Invalid index.")
        self._check_index(index)
        key = self.__heap[index]
        self.remove(index)
        return key

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
        return [i for i, k in enumerate(self.__heap) if k == key]

    def clear(self) -> None:
        self.__heap = []
        self.__size = 0
    # endregion public methods

    # region protected methods
    def _heapify_up(self, key: int, index: int) -> None:
        """
        Perform heapify-up operation to maintain the heap property after inserting a key at a specified index.

        Heapify-up is a recursive operation that compares the key with its parent in the heap and swaps them if
        * necessary.
        This process is repeated until the key is in its correct position or until it reaches the root of the heap
        * (index 0).

        Note:
        - This method assumes that the heap property is already satisfied for all indices below the specified index.

        :param key: The key value to be moved up.
        :param index: The current index at which the key is located in the heap.
        :return: None
        """
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if key > self.__heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(key, parent_index)

    def _heapify_down(self, key: int, index: int) -> None:
        """
        This method is used to heapify the elements downwards starting from the given index. It compares the key with
        * its left and right children, and if necessary, swaps the elements to ensure that the heap property is
        * maintained.

        Algorithm:
        1. Calculate the indices of the left and right children.
        2. If both children indices are -1, it means that there are no children and the method returns.
        3. If only the left child index is valid, compare the key with the left child. If the left child is greater,
           * swap the elements and return.
        4. If both children indices are valid, compare both children. If the left child is greater or equal to the right
           * child, compare the key with the left child. If it is greater, swap the elements and recursively call
           * _heapify_down() with the left child's index.
        5. If the right child is greater than the key, swap the elements and recursively call _heapify_down() with the
           * right child's index.

        :param key: The key value to be moved down.
        :param index: The current index at which the key is located in the heap.
        :return: None
        """
        left_child_index = 2 * index + 1 if 2 * index + 1 < self.__size else -1
        right_child_index = 2 * index + 2 if 2 * index + 2 < self.__size else -1
        if left_child_index == -1 and right_child_index == -1:
            return
        if left_child_index != -1 and right_child_index == -1:
            if self.__heap[left_child_index] > key:
                self._swap(index, left_child_index)
                return
            else:
                return
        if self.__heap[left_child_index] >= self.__heap[right_child_index]:
            if self.__heap[left_child_index] > key:
                self._swap(index, left_child_index)
                self._heapify_down(key, left_child_index)
        elif self.__heap[right_child_index] > key:
            self._swap(index, right_child_index)
            self._heapify_down(key, right_child_index)

    def _swap(self, index1: int, index2: int) -> None:
        """
        This method swaps the elements at the given indices in the heap.

        :param index1: The index of the first element to be swapped
        :param index2: The index of the second element to be swapped
        :return: None
        """
        temp = self.__heap[index1]
        self.__heap[index1] = self.__heap[index2]
        self.__heap[index2] = temp

    def _check_index(self, index: int) -> None:
        """
        Check if the index is valid for the Max-Heap.

        :param index: The index to be checked.
        :raises IndexError: If the Max-Heap is empty.
        :raises IndexError: If the index is invalid.
        :return: None
        """
        if self.__size == 0:
            raise IndexError("Max-Heap is empty.")
        if index < 0 or index >= self.__size:
            raise IndexError("Invalid index.")
    # endregion protected methods
