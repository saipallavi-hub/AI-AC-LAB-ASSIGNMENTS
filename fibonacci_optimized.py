#!/usr/bin/env python3
"""
Simplified Fibonacci: prints the first n terms directly from the main program
with minimal variables and no intermediate list.
"""

if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms (n >= 1): ").strip())
    except Exception:
        print("Invalid input: please enter a positive integer.")
        raise SystemExit(1)

    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        raise SystemExit(1)

    a, b = 0, 1
    for i in range(n):
        print(a, end=(" \n" if i == n - 1 else " "))
        a, b = b, a + b
