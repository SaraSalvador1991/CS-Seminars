class Node(object):
    __data = None
    __next = None

    def __init__(self, data=None):
        self.__next = None
        self.__data = data

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


if __name__ == '__main__':
    root = Node(11)
    new_node = Node('bliblablup')
    root.set_next(new_node)
    print(root.get_data())
    try:
        print(root.__data)
    except AttributeError:
        print("AttributeError")
    print(new_node.get_data())
    print(root.get_next().get_data())
    print(root.get_next())
    print(new_node.get_next())
