'''class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item) # queue where front is at positions -1, and back at position 0

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.isEmpty())
q.enqueue(8)
q.enqueue('bern')
print(q.dequeue())
print(q.dequeue())

# --------------------
class Queue_alt:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item) # queue where front is at positions 0, and back at position -1
        # NOTE: use append is better than insert. insert(-1) does not work to add element at the last position
        # since adding an element will increase the indices by one. Thus insert (-1) will put the element at the second last positon

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q=Queue_alt()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.isEmpty())
q.enqueue(8)
q.enqueue('bern')
print(q.dequeue())
print(q.dequeue())

# -----------------------

fruits = [91,9]

fruits.append(11)
#fruits.insert(-1, 11)
print(fruits)

# -----

# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')


print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1] # check the last element (the one that goes out)

    def size(self):
        return len(self.items)

s = Stack()
s.insert(4)
s.insert('dog')
print(s.peek())
s.insert(True)
print(s.size())
print(s.isEmpty())
s.insert(8.4)
print(s.delete())
print(s.delete())
print(s.size())

#x = [1,5,9,11,8,6,91,97]
#print(x[len(x)-1])
 #### ---

 # linked list
# create a class to represent your linked list: only information you need to store for a linked list is where the list starts
class LinkedList:
    def __init__(self):
        self.head = None # empty linked list

# Next, create another class to represent each node of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        def __repr__(self):
            return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList()
print(llist)
llist

first_node = Node("a")
llist.head = first_node
print(llist)


second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)