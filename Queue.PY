#Task-2 Queue Implementation
#write a python code Use AI to implement a Queue using Python lists.
#Sample Input Code:class Queue:pass
#Expected Output:FIFO-based queue class with enqueue, dequeue, peek, and size methods.
class Queue:
    """Queue using Python list"""
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "Queue empty"
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Front:", q.peek())
print("Removed:", q.dequeue())
print("Queue:", q.queue)