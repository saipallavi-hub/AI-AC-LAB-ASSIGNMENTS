#write a Python program Student class with name, roll number, and branch. It should also have a method to display the student details.”
class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")

# Example usage:
student1 = Student("Alice", "12345", "Computer Science")
student1.display_details()