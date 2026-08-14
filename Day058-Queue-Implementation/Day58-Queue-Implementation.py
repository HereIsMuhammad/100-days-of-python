# Day 58: Queue Implementation

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.popleft()
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", list(self.queue))


# Testing 
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()
q.display()

print("Front element:", q.peek())