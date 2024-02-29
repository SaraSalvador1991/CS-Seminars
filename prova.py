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
#class LinkedList:
    #def __init__(self):
        #self.head = None # empty linked list

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
first_node.next = second_node  # here the connection to the next one
second_node.next = third_node
print(llist)

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


    def get_data(self):
        return self.val


    def set_data(self, val):
        self.val = val


    def get_next(self):
        return self.next


    def set_next(self, next):
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.count = 0


    def insert(self, data):
        """
        Create a new node at the Head of the Linked List
        """
        # create a new node to hold the data
        new_node = Node(data)

        # set the next of the new node to the current head
        new_node.set_next(self.head)

        # set the head of the Linked List to the new head
        self.head = new_node

        # add 1 to the count
        self.count += 1


    def find(self, val):
        """
        Search for item in Linked List with data = val

        Time complexity is O(n) as in worst case scenario
        have to iterate over whole Linked List
        """
        # start with the first item in the Linked List
        item = self.head
        # then iterate over the next nodes
        # but if item = None then end search
        while item != None:

            # if the data in item matched val
            # then return item
            if item.get_data() == val:
                return item

            # otherwise we get the next item in the list
            else:
                item = item.get_next()

        # if while loop breaks with None then nothing found
        # so we return None
        return None


    def remove(self, item):
        """
        Remove Node with value equal to item
        Time complexity is O(n) as in the worst case we have to
        iterate over the whole linked list
        """

        # set the current node starting with the head
        current = self.head
        # create a previous node to hold the one before
        # the node we want to remove
        previous = None

        # while current is note None then we can search for it
        while current is not None:
            # if current equals to item then we can break
            if current.data == item:
                break
            # otherwise we set previous to current and
            # current to the next item in list
            previous = current
            current = current.get_next()

        # if the current is None then item, not in the list
        if current is None:
            raise ValueError(f"{item} is not in the list")
        # if previous None then the item is at the head
        if previous is None:
            self.head = current.next
            self.count -= 1
        # otherwise then we remove that node from the list
        else:
            previous.set_next(current.get_next())
            self.count -= 1


    def get_count(self):
        """
        Return the length of the Linked List
        Time complexity O(1) as only returning a single value
        """
        return self.count


    def is_empty(self):
        """
        Returns whether the Linked List is empty or not
        Time complexity O(1) as only returns True or False
        """
        # we only have to check the head if is None or not
        return self.head == None


def is_prime(self):
    if self == 1:
        return "False"
    for i in range(2, int(self**0.5)+1):
        if self % i == 0:
            return "False"
        else:
            return "True"

print(is_prime(3))


def is_prime(num):
    if num==1:
        return "False"
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return "False"
        else:
            return "True"

print(is_prime(9))
'''
import numpy
import matplotlib.pyplot as plt
class Circle:
    def __init__(self, radius1, radius2, center1_x, center1_y, center2_x, center2_y, theta):  ## theta in rad
        self.r1 = float(radius1)
        self.r2 = float(radius2)
        self.c1x = float(center1_x)
        self.c1y = float(center1_y)
        self.c2x = float(center2_x)
        self.c2y = float(center2_y)
        self.t = float(theta)

    def Circumference(self):  # function that calculate the circumference of a circle of radius r
        return round(2 * numpy.pi * self.r1, 3)

    def Area(self):  # function that calculate the area of a circle of radius r
        return round(numpy.pi * self.r1, 3)

    def Circumference_Sector(self):
        return self.r1 * self.t

    def Area_Sector(self):
        return round(self.r1 ** 2 / 2 * self.t, 3)

    def Intersect(self):
        dist = ((self.c1x - self.c2x) ** 2 + (self.c1y - self.c2y) ** 2) ** 0.5
        return round(dist,3)
        if dist <= self.r1 - self.r2:
            return ("Circle 2 is inside circle 1")
        elif dist <= self.r2 - self.r1:
            return ("Circle 1 is inside circle 1")
        elif dist < self.r1 + self.r2:
            return ("The two cricle intersect")
        elif dist == self.r1 + self.r2:
            return ("The two circle intersect in one point")
        else:
            return ("The two circles do not interect")

    def Graphic_prove(self):

        from matplotlib.patches import Circle

        plt.axis([-10, 10,-10,10])
        plt.axis("equal")
        c1 = (self.c1x,self.c1y)
        c2 = (self.c2x,self.c2y)
        circle1 = Circle(c1, self.r1, fill=False)
        circle2 = Circle(c2, self.r2, fill=False)

        plt.gca().add_artist(circle1)
        plt.gca().add_artist(circle2)
        plt.show()


c = Circle(6, 1, 0, 0, 1, 5, 1.5708)
print(c.Circumference())
print(c.Area())
print(c.Circumference_Sector())
print(c.Area_Sector())
print(c.Intersect())
c.Graphic_prove()

## check with the plot
'''
from matplotlib.patches import Circle

plt.axis([-10, 10, -10, 10])
plt.axis("equal")

center1 = (0, 0)
radius1 = 1
center2 = (1, 5)
radius2 = 1

circle1 = Circle(center1, radius1, fill=False)
circle2 = Circle(center2, radius2, fill=False)

plt.gca().add_artist(circle1)
plt.gca().add_artist(circle2)
plt.show()
'''








