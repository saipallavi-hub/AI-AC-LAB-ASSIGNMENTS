#Provide a Python snippet with a missing parenthesis in a printstatement like print "Hello". Use AI to detect and fix the syntax error.Use at least 3 assert test cases to confirm the corrected code works.Corrected code with proper syntax and AI explanation.
def greet():
   print("Hello, AI Debugging Lab!")
greet()
# The syntax error occurs because the print statement is not using parentheses, which is required in Python 3. In Python 2, print was a statement, but in Python 3, it is a function, so it must be called with parentheses.
def greet():
    print("Hello, AI Debugging Lab!")
# Test cases to verify the corrected function works properly
assert greet() is None  # The function should return None since it only prints a message    
# Additional test cases to ensure the function behaves as expected
import io
import sys
# Capture the output of the greet function
captured_output = io.StringIO()
sys.stdout = captured_output  # Redirect stdout to capture the print output
greet()  # Call the function to capture its output
sys.stdout = sys.__stdout__  # Reset redirect.
assert captured_output.getvalue() == "Hello, AI Debugging Lab!\n"  # Check if the output is correct
# Test case to ensure that the function does not return any value
assert greet() is None  # The function should return None since it only prints a message
print("All test cases passed!")