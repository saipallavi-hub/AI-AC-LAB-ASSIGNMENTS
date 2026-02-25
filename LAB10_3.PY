#TASK1: AI-Assisted Bug Detection
#The following Python function wrote by junior developer to calculate factorials:
"""def factorial(n):
    result = 1
  for i in range(1, n):
    result = result * i
return result"""
#Instructions:1. Run the code and test it with factorial(5),2. Use an AI assistant to: o Identify the logical bug in the code. o Explain why the bug occurs (e.g., off-by-one error). o Provide a corrected version.
#3. Compare the AI’s corrected code with your own manual fix., 4. Write a brief comparison: Did AI miss any edge cases (e.g., negative numbers, zero)?
#Expected Output: Corrected function should return 120 for factorial(5).
#Testing the original code
def factorial(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result
print(factorial(5))  # Output will be 24, which is incorrect
#AI-Assisted Bug Detection
#The logical bug in the code is that the loop runs from 1 to n-1, which means it does not include n in the multiplication. This results in an off-by-one error, causing the function to return 24 instead of 120 for factorial(5).
#Corrected version of the code
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Change the loop to include n
        result = result * i
    return result
print(factorial(5))  # Output will be 120, which is correct
#Comparison:
#The AI correctly identified the off-by-one error and provided a corrected version of the code.
# However, both the original and corrected versions do not handle edge cases such as negative numbers or zero. The factorial function should ideally return 1 for factorial(0) and raise an error for negative inputs. This is an area where the AI could have provided additional improvements to enhance the robustness of the code.
#Improved version with edge case handling
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result
print(factorial(5))  # Output will be 120
print(factorial(0))  # Output will be 1
try:
    print(factorial(-1))  # This will raise an error
except ValueError as e:
    print(e)  # Output will be "Factorial is not defined for negative numbers."

#task2: Improving Readability & Documentation
#following code is poorly written but works:
"""def calc(a, b, c):
if c == "add":
return a + b
elif c == "sub":
return a - b
elif c == "mul":
return a * b
elif c == "div":"""
#Instructions:
#5. Use AI to:
#-Critique the function’s readability, parameter naming, and lack of documentation.
#-Rewrite the function with:
#1. Descriptive function and parameter names.
#2. A complete docstring (description, parameters,return value, examples).
#3. Exception handling for division by zero.
#4. Consideration of input validation.
#6. Compare the original and AI-improved versions.
#7. Test both with valid and invalid inputs (e.g., division by zero, non-string operation).
#Expected Output:A well-documented, robust, and readable function that handles errors gracefully.
#test the original code
def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        return a / b
print(calc(10, 5, "add"))  # Output will be 15
print(calc(10, 5, "sub"))  # Output will be 5
print(calc(10, 5, "mul"))  # Output will be 50
print(calc(10, 5, "div"))  # Output will be 2.
#AI-Improved version of the code
def calculate(num1, num2, operation):
    """
    Performs a specified arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Must be one of "add", "subtract", "multiply", or "divide".

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If the operation is not recognized or if division by zero is attempted.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Supported operations are: add, subtract, multiply, divide.")
#Testing the AI-improved code
print(calculate(10, 5, "add"))  # Output will be 15
print(calculate(10, 5, "subtract"))  # Output will be 5
print(calculate(10, 5, "multiply"))  # Output will be 50
print(calculate(10, 5, "divide"))  # Output will be 2.0
try:
    print(calculate(10, 0, "divide"))  # This will raise an error
except ValueError as e:
    print(e)  # Output will be "Cannot divide by zero."
try:
    print(calculate(10, 5, "mod"))  # This will raise an error
except ValueError as e:
    print(e)  # Output will be "Invalid operation. Supported operations are: add, subtract, multiply, divide."
#Comparison:
#The original code lacked readability due to non-descriptive parameter names and no documentation. 
#It also did not handle edge cases such as division by zero or invalid operations. The AI-improved version addressed these issues by using descriptive names,  adding a comprehensive docstring, and implementing error handling for invalid inputs and division by zero, making the function more robust and user-friendly.
#Improved version with edge case handling
def calculate(num1, num2, operation):
    """
    Performs a specified arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Must be one of "add", "subtract", "multiply", or "divide".

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If the operation is not recognized or if division by zero is attempted.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Supported operations are: add, subtract, multiply, divide.")
    
#task3:Enforcing Coding Standards
#A developersubmits team project requires PEP8 compliance:
"""def Checkprime(n):
for i in range(2, n):
if n % i == 0:
return False
return True"""
#Instructions:
#8. Verify the function works correctly for sample inputs.
#9. Use an AI tool (e.g., ChatGPT, GitHub Copilot, or a PEP8 linter with AI explanation) to:
# -List all PEP8 violations.
# -Refactor the code (function name, spacing, indentation,naming).
#10. Apply the AI-suggested changes and verify functionality ispreserved.
#11. Write a short note on how automated AI reviews could streamline code reviews in large teams.
#Expected Output:
#A PEP8-compliant version of the function, e.g.:
"""def check_prime(n):
for i in range(2, n):
if n % i == 0:
return False
return True"""
#Testing the original code
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(Checkprime(5))  # Output will be True
print(Checkprime(10))  # Output will be False
#AI-PEP8 Violations:
#1. Function name should be in lowercase with words separated by underscores (check_prime instead of Checkprime).
#2. Missing spaces around operators (e.g., n % i should be n % i).
#3. Indentation should be consistent (4 spaces per indentation level).
#4. Missing docstring to explain the function's purpose and parameters.
#AI-Refactored code
def check_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check for primality.
    Returns:
        bool: True if n is prime, False otherwise.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#Testing the AI-refactored code
print(check_prime(5))  # Output will be True
print(check_prime(10))  # Output will be False
#Note on AI in code reviews:
#Automated AI reviews can significantly streamline code reviews in large teams by quickly identifying coding standard violations
#and providing suggestions for improvement. This can save time for human reviewers, allowing them to focus on more complex issues such as logic errors and architectural decisions. AI can also help maintain consistency across the codebase by enforcing coding standards and best practices, ultimately improving code quality and readability.
#Comparison:
#The original code had several PEP8 violations, including non-compliant function naming, lack of spacing around operators, 
# inconsistent indentation, and missing documentation. The AI-refactored code addressed all these issues by renaming the function to follow PEP8 guidelines, adding spaces around operators, ensuring consistent indentation, and including a docstring to explain the function's purpose and parameters. Both versions of the code preserved functionality, but the AI-refactored version is more readable and maintainable due to adherence to coding standards.
#improved version with edge case handling
def check_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check for primality.
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(check_prime(5))  # Output will be True
print(check_prime(10))  # Output will be False
print(check_prime(1))  # Output will be False
print(check_prime(0))  # Output will be False
print(check_prime(-5))  # Output will be False

#task4:AI as a Code Reviewer in Real Projects
#teammate submits a GitHub project
"""def processData(d):
return [x * 2 for x in d if x % 2 == 0]"""
#Instructions:
#1. Manually review the function for:
# - Readability and naming.
# - Reusability and modularity.
# -Edge cases (non-list input, empty list, non-integer elements).
#2. Use AI to generate a code review covering:
#a. Better naming and function purpose clarity.
#b. Input validation and type hints.
#c. Suggestions for generalization (e.g., configurable multiplier).
#3. Refactor the function based on AI feedback.
#4. Write a short reflection on whether AI should be a standalone reviewer or an assistant.
#Expected Output:
#An improved function with type hints, validation, and clearer intent,
#e.g.:
"""from typing import List, Union
def double_even_numbers(numbers: List[Union[int,
float]]) -> List[Union[int, float]]:
if not isinstance(numbers, list):
raise TypeError("Input must be a list")
return [num * 2 for num in numbers if isinstance(num,
(int, float)) and num % 2 == 0]"""
#Testing the original code
def processData(d):
    return [x * 2 for x in d if x % 2 == 0]
print(processData([1, 2, 3, 4, 5]))  # Output will be [4, 8]
#AI Code Review:
#a. The function name `processData` is vague and does not clearly indicate its purpose. A better name would be `double_even_numbers` to reflect that the function doubles the even numbers in the input list.
#b. The function lacks input validation and type hints. It should check if the input is a list and if the elements are integers or floats. Adding type hints would also improve readability and help with static analysis.
#c. The function could be generalized to allow for a configurable multiplier instead of hardcoding the value 2. This would make the function more flexible and reusable for different use cases.
#AI-Refactored code
from typing import List, Union
def double_even_numbers(numbers: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    """
    Doubles the even numbers in a list using a specified multiplier.

    Args:
        numbers (List[Union[int, float]]): A list of numbers to process.
        multiplier (Union[int, float], optional): The value to multiply the even numbers by. Defaults to 2.

    Returns:
        List[Union[int, float]]: A list of processed numbers where even numbers are multiplied by the multiplier.
    
    Raises:
        TypeError: If the input is not a list or if elements are not integers or floats.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    return [num * multiplier for num in numbers if isinstance(num, (int, float)) and num % 2 == 0]
#Testing the AI-refactored code
print(double_even_numbers([1, 2, 3, 4, 5]))  # Output will be [4, 8]
print(double_even_numbers([1, 2, 3, 4, 5], multiplier=3))  # Output will be [6, 12]
try:
    print(double_even_numbers("not a list"))  # This will raise an error
except TypeError as e:
    print(e)  # Output will be "Input must be a list"
try:
    print(double_even_numbers([1, 2, "three", 4, 5]))  # This will raise an error
except TypeError as e:
    print(e)  # Output will be "Input must be a list"
#Reflection on AI as a code reviewer:
#AI can be a valuable assistant in code reviews by quickly identifying issues related to readability, naming, and potential edge cases. It can provide suggestions for improvement and help enforce coding standards. However, AI should not be a standalone reviewer as it may miss context-specific nuances and complex logic that human reviewers can catch. Instead, AI should complement human reviews by handling routine checks and allowing human reviewers to focus on more critical aspects of the code, such as design decisions and overall architecture.
#improved version with edge case handling
from typing import List, Union
def double_even_numbers(numbers: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    """
    Doubles the even numbers in a list using a specified multiplier.

    Args:
        numbers (List[Union[int, float]]): A list of numbers to process.
        multiplier (Union[int, float], optional): The value to multiply the even numbers by. Defaults to 2.

    Returns:
        List[Union[int, float]]: A list of processed numbers where even numbers are multiplied by the multiplier.
    
    Raises:
        TypeError: If the input is not a list or if elements are not integers or floats.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    return [num * multiplier for num in numbers if isinstance(num, (int, float)) and num % 2 == 0]
print(double_even_numbers([1, 2, 3, 4, 5]))  # Output will be [4, 8]
print(double_even_numbers([1, 2, 3, 4, 5], multiplier=3))  # Output will be [6, 12]
try:
    print(double_even_numbers("not a list"))  # This will raise an error
except TypeError as e:
    print(e)  # Output will be "Input must be a list"
try:    print(double_even_numbers([1, 2, "three", 4, 5]))  # This will raise an error
except TypeError as e:
    print(e)  # Output will be "Input must be a list"

#task5:AI-Assisted Performance Optimization
#given a function that processes a list of integers, butit runs slowly on large datasets:
"""def sum_of_squares(numbers):
total = 0
for num in numbers:
total += num ** 2
return total"""
#Instructions:
#1. Test the function with a large list (e.g., range(1000000)).
#2. Use AI to:
#- Analyze time complexity.
#- Suggest performance improvements (e.g., using built-in functions, vectorization with NumPy if applicable).
#- Provide an optimized version.
#3. Compare execution time before and after optimization.
#4. Discuss trade-offs between readability and performance.
#Expected Output:
"""An optimized function, such as:
def sum_of_squares_optimized(numbers):
return sum(x * x for x in numbers)"""
#Testing the original code
import time
# Original Function
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
# Optimized Function (Correct Final Version)
def sum_of_squares_optimized(numbers):
    if not hasattr(numbers, "__iter__"):
        raise TypeError("Input must be an iterable of numbers.")
    return sum(x * x for x in numbers)
#Testing
large_data = range(1000000)
# Original Version Timing
start_time = time.time()
print("Original Result:", sum_of_squares(large_data))
end_time = time.time()
print("Execution time for original function:", end_time - start_time, "seconds")
# Optimized Version Timing
start_time = time.time()
print("Optimized Result:", sum_of_squares_optimized(large_data))
end_time = time.time()
print("Execution time for optimized function:", end_time - start_time, "seconds")