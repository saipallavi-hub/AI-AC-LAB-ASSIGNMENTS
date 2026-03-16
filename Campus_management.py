#Task-9 Real-Time Application Challenge – Choose the Right Data Structure
#cenario:college wants to develop a Campus Resource Management System that handles:
#1.Student Attendance Tracking – Daily log of students entering/exiting the campus,2.Event Registration System – Manage participants in events with quick search and removal.3.Library Book Borrowing – Keep track of available books and their due dates. Bus Scheduling System – Maintain bus routes and stop connections. 5.Cafeteria Order Queue – Serve students in the order they arrive.
#Student Task:For each feature, select the most appropriate data structure fromthe list below:
#Stack,Queue,Priority Queue,Linked List,Binary Search Tree (BST),Graph,Hash Table,Deque
#Justify your choice in 2–3 sentences per feature.Implement one selected feature as a working Python program with AI-assisted code generation.
#Expected Output:A table mapping feature → chosen data structure → justification.A functional Python program implementing the chosen feature with comments and docstrings.

class CafeteriaQueue:
    """Queue implementation for managing cafeteria orders.
    Students are served in the order they arrive (FIFO principle)."""

    def __init__(self):
        self.orders = []

    def place_order(self, student_name):
        """Add a new order to the queue"""
        self.orders.append(student_name)
        print(student_name, "placed an order.")

    def serve_order(self):
        """Serve the first order in the queue"""
        if len(self.orders) == 0:
            print("No orders to serve.")
        else:
            served = self.orders.pop(0)
            print(served, "order served.")

    def display_orders(self):
        """Display all current orders"""
        print("Current Orders:", self.orders)


# Example usage
queue = CafeteriaQueue()

queue.place_order("Rahul")
queue.place_order("Anita")
queue.place_order("Kiran")

queue.display_orders()

queue.serve_order()
queue.display_orders()