#Task-1 Stack Implementation
#write a python code Use AI to generate a Stack class with push, pop, peek, and is_empty methods.
#Sample Input Code:class Stack:pass
#Expected Output:functional stack implementation with all required methods and docstrings.'
class Stack:
    """Stack Data Structure"""
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    def is_empty(self):
        return len(self.stack) == 0
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element:", s.peek())
print("Removed:", s.pop())
print("Stack:", s.stack)