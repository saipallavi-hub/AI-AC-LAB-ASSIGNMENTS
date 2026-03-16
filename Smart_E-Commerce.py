#Task-10 Smart E-Commerce Platform – Data Structure Challenge
#An e-commerce company wants to build a Smart Online Shopping System with:1.Shopping Cart Management – Add and remove productsdynamically.Order Processing System – Orders processed in the order they are placed.3.Top-Selling Products Tracker – Products ranked by sales count.4..Product Search Engine – Fast lookup of products using product ID. 5.Delivery Route Planning – Connect warehouses and delivery locations.
#Student Task: For each feature, select the most appropriate data structure from the list below:
#Stack,Queue,Priority Queue, Linked List,Binary Search Tree (BST),Graph,Hash Table,Deque
#Justify your choice in 2–3 sentences per feature.Implement one selected feature as a working Python program with AI-assisted code generation.
#Expected Output:
#A table mapping feature → chosen data structure → justification.
#A functional Python program implementing the chosen feature with comments and docstrings.
class OrderQueue:
    """
    Queue implementation for processing e-commerce orders.
    Orders are processed in FIFO order.
    """

    def __init__(self):
        self.orders = []

    def add_order(self, order_id):
        """Add a new order to the system"""
        self.orders.append(order_id)
        print("Order", order_id, "added.")

    def process_order(self):
        """Process the first order"""
        if len(self.orders) == 0:
            print("No orders to process.")
        else:
            order = self.orders.pop(0)
            print("Processing Order:", order)

    def show_orders(self):
        """Display pending orders"""
        print("Pending Orders:", self.orders)


# Example usage
orders = OrderQueue()

orders.add_order(101)
orders.add_order(102)
orders.add_order(103)

orders.show_orders()

orders.process_order()
orders.show_orders()