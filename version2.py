def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4
    - But not divisible by 100, unless it is also divisible by 400
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4
    - But not divisible by 100, unless it is also divisible by 400
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input with error handling
try:
    year = int(input("Enter a year: "))
    if year < 0:
        print("Please enter a positive year.")
    else:
        # Check and display result
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid integer year.")