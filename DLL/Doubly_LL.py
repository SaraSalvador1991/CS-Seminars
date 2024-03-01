from typing import Any
from DLL.Node import Node


class DoublyLinkedList(object):
    """
    :class: DoublyLinkedList
    A class representing a doubly linked list data structure.

    The DoublyLinkedList class provides methods to manipulate the  doubly linked list such as appending data, inserting data at a
    * given index, removing data, removing an index, getting the data at a given index, and printing the data in the
    * doubly linked list.

    The DoublyLinkedList class has the following attributes:
    - `head`: A reference to the first node in the doubly linked list.
    - `tail`: A reference to the last node in the doubly linked list.
    - `size`: The number of elements in the doubly linked list.

    The DoublyLinkedList class has the following methods:
    - `get_size`: Returns the size of the doubly linked list.
    - `append`: Appends data to the end of the doubly linked list.
    - `insert`: Inserts data at a given index in the doubly linked list.
    - `remove_data`: Removes the first appearance of data from the doubly linked list.
    - `remove_index`: Removes the specified index from the doubly linked list.
    - `get_data_at_index`: Returns the data at the given index.
    - `print_ll_data`: Prints the data of the current doubly linked list.

    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        """
        Returns the size of the doubly linked list.
        :return: Number of elements in the doubly linked list.
        """
        return self.size

    def append(self, data: Any) -> None:
        """
        Appends data to the end of the doubly linked list.
        :param data: Data to be appended.
        """
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node
        self.size += 1

    def insert(self, data: Any, index: int) -> None:
        """
        Inserts data at a given index in the doubly linked list.
        :param data: Data to be inserted.
        :param index: Index between 0 and size of the doubly linked list.
        """
        if index == self.size:
            self.append(data)
            return
        node = Node(data)
        if index == 0:
            node.set_next(self.head)
            self.head.set_prev(node)  ### new line
            self.head = node
            self.size += 1
        elif 0 < index < self.size:
            iter_node = self.head
            for _ in range(0, index - 1):
                iter_node = iter_node.get_next()
            node.set_next(iter_node.get_next())
            node.set_prev(iter_node)    ## new line
            iter_node.get_next().set_prev(node)     ## new line
            iter_node.set_next(node)
            self.size += 1
        else:
            print(f"Given index is not valid. Current size of the doubly linked list is {self.size}.")


    def remove_data(self, data: Any) -> None:
        """
        Removes/Deletes the first appearance of data from the  doubly linked list.
        :param data: Data to be removed
        """
        if self.size == 0:
            print("Cannot remove data. Doubly linked List is empty.")
            return
        data_found = False
        current_node = self.head
        previous_node = self.head
        index = 0
        while current_node is not None and data_found is False:
            if current_node.get_data() == data:
                data_found = True
                print(f"Removed data '{data}'.")
                previous_node.set_next(current_node.get_next())
                next_node= current_node.get_next()      ## new line
                # next_node.set_prev(current_node.get_prev())        ## new line
                next_node.set_prev(previous_node)  ### Line 103 can be simplified
                self.size -= 1
                if self.size == 0:
                    self.head = None
                    self.tail = None
                elif index == self.size:
                    self.tail = previous_node
                    self.tail.set_next(None) ## after the (new) tail, None
                elif index == 0:
                    self.head = previous_node.get_next()  # or 'self.head = current_node.get_next()'
                    self.head.set_prev(None) ## before the (new) head, None
            else:
                previous_node = current_node
                current_node = current_node.get_next()
                index += 1
        if not data_found:
            raise ValueError(f"Data '{data}' not found.")

    def remove_index(self, index: int) -> None:
        """
        Removes/Deletes the specified index from the doubly linked list.
        :param index: Index between 0 and size-1 of the doubly linked list.
        """
        if 0 <= index < self.size:
            current_node = self.head
            previous_node = self.head
            for _ in range(0, index):
                previous_node = current_node
                current_node = current_node.get_next()
            print(f"Removed index {index}.")
            previous_node.set_next(current_node.get_next())
            next_node = current_node.get_next()  ## new line
            # next_node.set_prev(current_node.get_prev())  ## new line
            next_node.set_prev(previous_node)  ### Same as line 103
            self.size -= 1
            if self.size == 0:
                self.head = None
                self.tail = None
            elif index == self.size:
                self.tail = previous_node
                self.tail.set_next(None) ## new line, as above
            elif index == 0:
                self.head = previous_node.get_next()  # or 'self.head = current_node.get_next()'
                self.head.set_prev(None)  ## new line, as above
        else:
            raise IndexError(f"Given index is not valid. Current size of the doubly linked list is {self.size}.")

    def get_data_at_index(self, index: int) -> Any:
        """
        Returns the data at the given index.
        :param index: Index between 0 and size-1 of the doubly linked list.
        :return: If the index is valid, returns the data at the given index.
        """
        if 0 <= index < self.size:
            current_node = self.head
            for _ in range(0, index):
                current_node = current_node.get_next()
            return current_node.get_data()
        else:
            raise IndexError(f"Given index is not valid. Current size of the doubly linked list is {self.size}.")


    def print_dll_data(self) -> None:
        """
        Prints the data of the current doubly linked list line by line in the form <Index i: data>.
        """
        if self.size == 0:
            print("Doubly linked List is empty.")
            return
        index = 0
        node = self.head
        print("--------------------")
        # print(f"Head data: {self.head.get_data()}")
        while node is not None:
            print(f"Index {index}: {node.get_data()}")
            index += 1
            node = node.get_next()
        # print(f"Tail data: {self.tail.get_data()}")
        print("--------------------")
