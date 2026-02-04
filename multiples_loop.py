#Write a Python that prints the first 10 multiples of a given number using a for loop.
number = int(input("Enter a number: "))
print(f"The first 10 multiples of {number} are:")
for i in range(1, 11):
    multiple = number * i
    print(multiple)

