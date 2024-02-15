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
    print("My age is " + self.age)

p1 = Person("John", 36)
p1.myfunc()

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
        self.items.insert(0,item)

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
print(q.dequeue())
q.dequeue()




