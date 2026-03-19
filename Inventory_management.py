#Task 4 (Real-Time Application – Inventory Management System)
#Scenario: A retail store’s inventory system contains thousands of products, each with attributes like product ID, name, price, and stock quantity. Store staff need to:
#Quickly search for a product by ID or name,Sort products by price or quantity for stock analysis.
#Task: Use AI to suggest the most efficient search and sort algorithms for this use case,Implement the recommended algorithms in Python,Justify the choice based on dataset size, update frequency, and performance requirements.
#Expected Output:A table mapping operation → recommended algorithm → justification,Working Python functions for searching and sorting the inventory.
products = [
    {"id": 1, "name": "Laptop", "price": 50000, "qty": 10},
    {"id": 2, "name": "Phone", "price": 20000, "qty": 50},
    {"id": 3, "name": "Tablet", "price": 30000, "qty": 20}
]

# Hash Map for search
product_map = {p["id"]: p for p in products}

def search_by_id(pid):
    return product_map.get(pid, "Not Found")

def sort_by_price(products):
    return sorted(products, key=lambda x: x["price"])

print(search_by_id(2))
print(sort_by_price(products))