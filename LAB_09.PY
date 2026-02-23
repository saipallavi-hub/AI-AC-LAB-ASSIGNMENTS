#Lab 9: Documentation Generation – Automatic Documentation and Code Comments
#task description #1 
#Write a Python function to return the sum of even numbers and sum of odd numbers in a given list.Generate a Google-style Python docstring for the following function.
#The docstring should include:A clear description of the function’s purpose,Args section with parameter
# names and types,Returns section with types and descriptions
def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a given list.

    Args:
        numbers (list): A list of integers to be processed.
    Returns:
        tuple: A tuple containing two elements:
            - sum_even (int): The sum of all even numbers in the list.
            - sum_odd (int): The sum of all odd numbers in the list.
    """
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    return sum_even, sum_odd    
#Example usage:
numbers = [1, 2, 3, 4, 5, 6]
even_sum, odd_sum = sum_even_odd(numbers)
print(f"Sum of even numbers: {even_sum}")  # Output: Sum of even numbers: 12
print(f"Sum of odd numbers: {odd_sum}")    # Output: Sum of odd numbers: 9

#task description #2
#You are developing a student management module that must be easy to understand for new developers.
#Requirements:Attributes: name, roll_no, hostel_status, Methods: fee_update() and display_details(), Manually write inline comments for each line or logical block, Use an AI-assisted tool to automatically add inline comments, Compare manual comments with AI-generated comments, Identify missing, redundant, or incorrect AI comments
class Student:
    def __init__(self, name: str, roll_no: int, hostel_status: bool):
        # Initialize the Student object with name, roll number, and hostel status
        self.name = name  # Store the student's name
        self.roll_no = roll_no  # Store the student's roll number
        self.hostel_status = hostel_status  # Store whether the student is in a hostel or not
    def fee_update(self, new_fee: float):
        # Update the fee for the student (this is a placeholder method)
        pass  # This method can be implemented to update the fee based on certain conditions
    def display_details(self):
        # Display the details of the student
        print(f"Name: {self.name}")  # Print the student's name
        print(f"Roll No: {self.roll_no}")  # Print the student's roll number
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")  # Print whether the student is in a hostel or not 
#Example usage:
student1 = Student("Alice", 101, True)
student1.display_details()  # Output: Name: Alice, Roll No: 101, Hostel Status: Yes 

#task description #3
#You are building a small calculator module that will be shared across multiple projects and requires structured documentation.
#Write a Python script containing 3–4 functions (e.g., add, subtract, multiply, divide),Manually write NumPy Style docstrings for each function,Use AI assistance to generate:,A module-level docstring
#Individual function-level docstrings,Evaluate documentation structure, accuracy, and readability
"""
Calculator Module
This module provides basic arithmetic operations such as addition,
subtraction, multiplication, and division.
"""

def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide the first number by the second."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# --------- Execute Functions to Get Output ---------
if __name__ == "__main__":
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))