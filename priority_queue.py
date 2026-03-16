#Lab-7 Priority Queue
#write a python code Use AI to implement a priority queue using Python’s heapq module.
#Sample Input Code:class PriorityQueue:pass
#Expected Output:Implementation with enqueue (priority), dequeue (highest priority),and display methods.
import heapq

class PriorityQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]


pq = PriorityQueue()

pq.enqueue("Task1", 2)
pq.enqueue("Task2", 1)

print("Removed:", pq.dequeue())