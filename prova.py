class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop() # pop the last item? should pop the first

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

# -----------------------

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
queue.append('d')
print("\nQueue after removing elements")
print(queue)

