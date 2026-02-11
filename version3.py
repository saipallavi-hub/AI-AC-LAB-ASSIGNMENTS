import calendar

def is_leap_year(year):
    """
    Check if a given year is a leap year using Python's calendar module.
    """
    return calendar.isleap(year)

# Get user input
year = int(input("Enter a year: "))

# Check and display result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")