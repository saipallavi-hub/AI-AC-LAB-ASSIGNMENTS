def print_fibonacci(n):
    """Print Fibonacci sequence up to n terms (n >= 1)."""
    a, b = 0, 1
    for i in range(n):
        # print current term followed by space (except final newline)
        end_char = ' ' if i < n - 1 else '\n'
        print(a, end=end_char)
        a, b = b, a + b


if __name__ == '__main__':
    try:
        n = int(input("Enter number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print_fibonacci(n)
    except ValueError:
        print("Invalid input; please enter an integer.")
