#Task-8 Deque
#write a python code Use AI to implement a double-ended queue using collections deque.
#ample Input Code:class DequeDS:pass
#xpected Output:Insert and remove from both ends with docstrings.
from collections import deque

class DequeDS:

    def __init__(self):
        self.dq = deque()

    def insert_front(self, item):
        self.dq.appendleft(item)

    def insert_rear(self, item):
        self.dq.append(item)

    def remove_front(self):
        return self.dq.popleft()

    def remove_rear(self):
        return self.dq.pop()


d = DequeDS()

d.insert_front(10)
d.insert_rear(20)

print("Deque:", d.dq)
print("Removed front:", d.remove_front())
