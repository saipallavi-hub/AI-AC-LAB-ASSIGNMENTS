"""Iterative and recursive Fibonacci sequence generators.
Accepts user input for number of terms and prints the sequence on one line.
"""

from typing import List


def fib_iter(n: int) -> List[int]:
    """Return first n Fibonacci numbers using an iterative approach."""
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def fib_rec(n: int) -> List[int]:
    """Return first n Fibonacci numbers using a recursive approach that builds the sequence."""
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = fib_rec(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    try:
        n_str = input("Enter number of terms: ").strip()
        n = int(n_str)
        if n < 0:
            raise ValueError("n must be non-negative")
    except ValueError:
        print("Please enter a non-negative integer.")
    else:
        sequence = fib_rec(n)
        # Print sequence in one line separated by spaces; print empty line for n=0
        print(" ".join(str(x) for x in sequence))
