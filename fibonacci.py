#!/usr/bin/env python3
"""
Print the Fibonacci sequence up to n terms.
Accepts user input for n. Logic is implemented directly in main (no user-defined functions).
"""

if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms (n >= 1): ").strip())
    except ValueError:
        print("Invalid input: please enter a positive integer.")
        raise SystemExit(1)

    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        raise SystemExit(1)

    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(str(a))
        a, b = b, a + b

    print(f"Fibonacci sequence (first {n} terms):")
    print(" ".join(seq))
