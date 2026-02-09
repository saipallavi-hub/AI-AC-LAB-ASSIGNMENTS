#correct the code and verify the corrected version using 3 assert test cases.Find and explain the error in the following Python code where = is used instead of == in an if condition.
def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"
# The error in the original code is that it uses a single equals sign (=) instead of a double equals sign (==) in the if condition. In Python, a single equals sign is used for assignment, while a double equals sign is used for comparison. Using a single equals sign in an if condition will result in a syntax error because it is not valid to assign a value within an if statement.
# Test cases to verify the corrected function works properly    
assert check_number(10) == "Ten"  # Test case where n is equal to 10
assert check_number(5) == "Not Ten"  # Test case where n is not equal to 10
assert check_number(0) == "Not Ten"  # Test case where n is not equal to 10
print("All test cases passed!") 
# In the corrected code, we use the double equals sign (==) to compare the value of n with 10. This allows the function to correctly determine whether n is equal to 10 and return the appropriate string. The assert statements confirm that the function behaves as expected for different input values.  
