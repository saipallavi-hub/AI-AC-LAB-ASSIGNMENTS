#generate an Armstrong number checking functionwith comments and explanations. give the code line-by-line Compare the explanation with code functionality.
def is_armstrong_number(num):
    """
    This function checks if a given number is an Armstrong number.
    An Armstrong number for a given number of digits is an integer such that the sum of its own digits each raised to the power of the number of digits is equal to the number itself.
    
    For example:
    - 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153
    - 9474 is an Armstrong number because 9^4 + 4^4 + 7^4 + 4^4 = 9474
    """
    
    # Convert the number to string to easily iterate over each digit
    digits = str(num)
    
    # Calculate the number of digits
    num_digits = len(digits)
    
    # Initialize sum to store the sum of each digit raised to the power of num_digits
    sum_of_powers = 0
    
    # Iterate over each digit in the number
    for digit in digits:
        # Convert the character back to integer and raise it to the power of num_digits
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the calculated sum is equal to the original number
    return sum_of_powers == num
# Example usage:
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
# Example usage:
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")

else:
    print(f"{number} is not an Armstrong number.")