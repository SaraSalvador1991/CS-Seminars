# class

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# -------

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# ----------

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

  def myfunc2(self):
    print("I am", self.age, "years old")

p1 = Person("Sara", 32)
p1.myfunc()
p1.myfunc2()

# --------
# queue
# initialize the queue

queue = []

# add element to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)

#removing element from the queue

print("\nElements dequeued from queue")
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

# ----------------

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item) # queue where front is at positions 0, and back at position -1 (last item)
        # NOTE: use append is better than insert. insert(-1) does not work to add element at the last position
        # since adding an element will increase the indices by one. Thus insert (-1) will put the element at the second last positon

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.isEmpty()) # queue [4,dog,true]
#print(q.dequeue())
q.enqueue(8) # insert now 8 at the back: the queue becomes [dog,true,8]
print(q.size())
print(q.dequeue()) # the element popped is the one that first entered the queue, hence 4
q.enqueue('Thun') # I insert now another element: it enters the queue last, so 'dog' will go out
print(q.dequeue()) # dog

# other example

q=Queue() # queue with 4 elements
q.enqueue(11)
q.enqueue('cat')
q.enqueue(True)
q.enqueue('Bern')
print(q.isEmpty())
q.enqueue('Thun')
print(q.dequeue())


# ----- stack

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

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
# ---------

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
s.insert(11)
s.insert("cat")
s.insert("Thun")
print(s.isEmpty())
print(s.peek())
s.delete()
s.insert("Bern")
print(s.peek())
print(s.size())


# -------------------------------
# Linked lists

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
first_node.next = second_node  # here the connection to the next one
second_node.next = third_node
print(llist)

