from typing import Any
from DLL.Node import Node


class LinkedList(object):
    """
    :class: LinkedList
    A class representing a linked list data structure.

    The LinkedList class provides methods to manipulate the linked list such as appending data, inserting data at a
    * given index, removing data, removing an index, getting the data at a given index, and printing the data in the
    * linked list.

    The LinkedList class has the following attributes:
    - `head`: A reference to the first node in the linked list.
    - `tail`: A reference to the last node in the linked list.
    - `size`: The number of elements in the linked list.

    The LinkedList class has the following methods:
    - `get_size`: Returns the size of the linked list.
    - `append`: Appends data to the end of the linked list.
    - `insert`: Inserts data at a given index in the linked list.
    - `remove_data`: Removes the first appearance of data from the linked list.
    - `remove_index`: Removes the specified index from the linked list.
    - `get_data_at_index`: Returns the data at the given index.
    - `print_ll_data`: Prints the data of the current linked list.

    Example usage:
    ```
    # Create a new linked list
    linked_list = LinkedList()

    # Append data to the linked list
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Insert data at a given index in the linked list
    linked_list.insert(0, 0)
    linked_list.insert(4, 4)

    # Remove data from the linked list
    linked_list.remove_data(2)

    # Remove an index from the linked list
    linked_list.remove_index(0)

    # Get the data at a given index in the linked list
    data = linked_list.get_data_at_index(0)

    # Print the data in the linked list
    linked_list.print_ll_data()
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        """
        Returns the size of the linked list.
        :return: Number of elements in the linked list.
        """
        return self.size

    def append(self, data: Any) -> None:
        """
        Appends data to the end of the linked list.
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
        Inserts data at a given index in the linked list.
        :param data: Data to be inserted.
        :param index: Index between 0 and size of the linked list.
        """
        if index == self.size:
            self.append(data)
            return
        node = Node(data)
        if index == 0:
            node.set_next(self.head)
            self.head = node
            self.size += 1
        elif 0 < index < self.size:
            iter_node = self.head
            for _ in range(0, index - 1):
                iter_node = iter_node.get_next()
            node.set_next(iter_node.get_next())
            node.set_prev(iter_node)
            iter_node.get_next().set_previous(node)
            iter_node.set_next(node)
            self.size += 1
        else:
            print(f"Given index is not valid. Current size of linked list is {self.size}.")


## okay untill here

    def remove_data(self, data: Any) -> None:   # should change this
        """
        Removes/Deletes the first appearance of data from the linked list.
        :param data: Data to be removed
        """
        if self.size == 0:
            print("Cannot remove data. Linked List is empty.")
            return
        data_found = False
        current_node = self.head
        previous_node = self.head
        index = 0
        while current_node is not None and data_found is False:
            if current_node.get_data() == data:
                data_found = True
                print(f"Removed data '{data}'.")
                previous_node.set_next(current_node.get_next())  ## here change
                self.size -= 1
                if self.size == 0:
                    self.head = None
                    self.tail = None
                elif index == self.size:
                    self.tail = previous_node
                elif index == 0:
                    self.head = previous_node.get_next()  # or 'self.head = current_node.get_next()'
            else:
                previous_node = current_node
                current_node = current_node.get_next() ## here
                index += 1
        if not data_found:
            raise ValueError(f"Data '{data}' not found.")

    def remove_index(self, index: int) -> None:   ## should this change?
        """
        Removes/Deletes the specified index from the linked list.
        :param index: Index between 0 and size-1 of the linked list.
        """
        if 0 <= index < self.size:
            current_node = self.head
            previous_node = self.head
            for _ in range(0, index):
                previous_node = current_node
                current_node = current_node.get_next()
            print(f"Removed index {index}.")
            previous_node.set_next(current_node.get_next())
            self.size -= 1
            if self.size == 0:
                self.head = None
                self.tail = None
            elif index == self.size:
                self.tail = previous_node
            elif index == 0:
                self.head = previous_node.get_next()  # or 'self.head = current_node.get_next()'
        else:
            raise IndexError(f"Given index is not valid. Current size of linked list is {self.size}.")

    def get_data_at_index(self, index: int) -> Any: ## also this? in my opinion not
        """
        Returns the data at the given index.
        :param index: Index between 0 and size-1 of the linked list.
        :return: If the index is valid, returns the data at the given index.
        """
        if 0 <= index < self.size:
            current_node = self.head
            for _ in range(0, index):
                current_node = current_node.get_next()
            return current_node.get_data()
        else:
            raise IndexError(f"Given index is not valid. Current size of linked list is {self.size}.")


   ## this should remain as before

    def print_ll_data(self) -> None:
        """
        Prints the data of the current linked list line by line in the form <Index i: data>.
        """
        if self.size == 0:
            print("Linked List is empty.")
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
