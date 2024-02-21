from node import Node


class LinkedList(object):
    head = None
    tail = None
    size = 0

    def __init__(self):
        self.head = self.tail
        self.tail = self.head

    def get_size(self) -> int:
        return self.size

    def append(self, data) -> None:
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node
        self.size += 1

    def insert(self, data, index: int) -> None:
        # TODO: Implement function
        pass

    def remove_data(self, data) -> None:
        if self.size == 0:
            print("Cannot remove data. Linked List is empty.")
            return

        data_found = False
        current_node = self.head
        previous_node = self.head
        while current_node is not None and data_found is False:
            if current_node.get_data() == data:
                data_found = True
                previous_node.set_next(current_node.get_next())
                print(f"Removed data '{data}'.")
                self.size -= 1
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if not data_found:
            print(f"Data '{data}' not found.")

    def remove_index(self, index: int) -> None:
        # TODO: Implement function
        pass

    def print_ll_data(self) -> None:
        if self.size == 0:
            print("Linked List is empty.")
            return

        index = 0
        node = self.head
        while node is not None:
            print(f"Index {index}: {node.get_data()}")
            index += 1
            node = node.get_next()


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
    ll.remove_data(44)
    ll.remove_data('hahaha')

    ll2 = LinkedList()
    ll2.remove_data(100)
    ll2.append(100)
    ll2.print_ll_data()
    ll2.remove_data(100)
    ll2.print_ll_data()
