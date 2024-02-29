from typing import Any
from classes.node import Node


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
            iter_node.set_next(node)
            self.size += 1
        else:
            print(f"Given index is not valid. Current size of linked list is {self.size}.")

    def remove_data(self, data: Any) -> None:
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
                previous_node = current_node
                current_node = current_node.get_next()
                index += 1
        if not data_found:
            raise ValueError(f"Data '{data}' not found.")

    def remove_index(self, index: int) -> None:
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

    def get_data_at_index(self, index: int) -> Any:
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


if __name__ == '__main__':
    ll = LinkedList()
    ll.print_ll_data()
    print(ll.get_size())
    ll.append(11)
    print(ll.get_size())
    ll.print_ll_data()
    ll.append('bliblablup')
    print(ll.get_size())
    ll.print_ll_data()
    ll.append(22)
    ll.append('haha')
    ll.append(33)
    ll.print_ll_data()
    ll.remove_data(22)
    ll.print_ll_data()
    a = 44
    try:
        ll.remove_data(a)
    except ValueError:
        print(f"A ValueError was raised as expected. Data {a} not found.")
    a = 'hahaha'
    try:
        ll.remove_data(a)
    except ValueError:
        print(f"A ValueError was raised as expected. Data {a} not found.")

    ll2 = LinkedList()
    ll2.remove_data(100)
    ll2.append(100)
    ll2.print_ll_data()
    ll2.remove_data(100)
    ll2.print_ll_data()

    ll3 = LinkedList()
    ll3.insert(55, 0)
    ll3.print_ll_data()
    ll3.insert(66, 0)
    ll3.print_ll_data()
    ll3.insert(77, ll3.get_size())
    ll3.print_ll_data()
    ll3.insert(88, 1)
    ll3.print_ll_data()
    ll3.insert(99, 2)
    ll3.print_ll_data()
    ll3.insert(111, 6)
    ll3.remove_data(99)
    ll3.print_ll_data()
    ll3.insert(111, ll3.get_size() - 1)
    ll3.print_ll_data()

    ll4 = LinkedList()
    a = 0
    try:
        ll4.remove_index(a)
    except IndexError:
        print(f"An IndexError was raised as expected. Index {a} not found.")
    ll4.append('a')
    ll4.print_ll_data()
    ll4.remove_index(0)
    ll4.print_ll_data()
    ll4.append('b')
    ll4.append('c')
    ll4.print_ll_data()
    ll4.remove_index(0)
    ll4.print_ll_data()
    ll4.append('d')
    ll4.append('e')
    ll4.append('f')
    ll4.append('g')
    ll4.print_ll_data()
    ll4.remove_index(ll4.get_size()-1)
    ll4.print_ll_data()
    ll4.remove_index(2)
    ll4.print_ll_data()
    try:
        ll4.remove_index(ll4.get_size())
    except IndexError:
        print(f"An IndexError was raised as expected. Index {ll4.get_size()} not found.")

    ll5 = LinkedList()
    ll5.append(1234)
    ll5.append('Everyone')
    ll5.append("Everyone who helped has been rewarded.")
    ll5.append(["I successfully completed a map", 9876, oct(10), [1, 2, 3]])
    ll5.append(0xDA)
    ll5.print_ll_data()
    get_data = ll5.get_data_at_index(2)
    print(get_data)
    print(ll5.get_data_at_index(0))
    ll5.print_ll_data()
    ll5.remove_data(1234)
    ll5.print_ll_data()
    ll5.remove_data(0xDA)
    ll5.print_ll_data()
