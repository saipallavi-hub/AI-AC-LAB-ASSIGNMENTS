#correct the python code using type casting and string concatenation, and verify both solutions using 3 assert test cases.The following Python code throws a TypeError because it tries to add a string and an integer. Please explain the error.
def add_five(value):
    return int(value) + 5
print(add_five("10"))
# The error occurs because the function add_five is trying to add an integer (5) to a string ("10"). In Python, you cannot directly add a string and an integer together, which results in a TypeError. To fix this issue, we can either convert the string to an integer before adding or convert the integer to a string and concatenate them.
# Solution 1: Convert the string to an integer  
def add_five(value):
    return int(value) + 5
# Test cases to verify the corrected function works properly
assert add_five("10") == 15  # Test case where value is a string
assert add_five("0") == 5    # Test case where value is a string representing zero
assert add_five("-5") == 0   # Test case where value is a string representing a negative number
print("All test cases for Solution 1 passed!")
# Solution 2: Convert the integer to a string and concatenate
def add_five(value):
    return str(value) + "5"
# Test cases to verify the corrected function works properly
assert add_five("10") == "105"  # Test case where value is a string
assert add_five("0") == "05"    # Test case where value is a string representing zero
assert add_five("-5") == "-55"   # Test case where value is a string representing a negative number
print("All test cases for Solution 2 passed!")  
# In Solution 1, we convert the input value to an integer using int() before adding 5, which allows us to perform the addition correctly. In Solution 2, we convert the integer 5 to a string and concatenate it with the input value, which results in a new string. Both solutions address the TypeError and allow the function to work as intended. The assert statements confirm that both solutions produce the expected results for different test cases.
