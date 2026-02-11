# Comparison: Inline vs Function-based Fibonacci ✅

## Summary
- **`fibonacci.py`**: logic implemented inline in the `__main__` block (no user-defined functions). It reads user input, builds a list of terms, and prints them.
- **`fibonacci_function.py`**: encapsulates the sequence printing in a dedicated function `print_fibonacci(n)`, with the `__main__` block handling input and validation.

---

## Quick comparison (concise table) 📊

| Aspect | Inline (`fibonacci.py`) | Function-based (`fibonacci_function.py`) |
|---|---:|---|
| **Readability** | Simple to follow for very short scripts; logic and IO mixed. | Clearer separation: core logic in a named function. |
| **Reusability** | Low — logic tied to script execution & direct printing. | High — function can be imported and reused. |
| **Testability** | Harder to test; relies on I/O and script run. | Easier to test if function returns data or has small side effects. |
| **Separation of concerns** | Input, computation, and output are mixed. | Better: input handled in `__main__`, computation in function. |
| **Extensibility** | More fragile when extending (e.g., changing output format). | Easier to extend (e.g., add variants or return values). |
| **Performance** | Same algorithmic performance (both iterative O(n), O(1) extra memory). | Same. |

---

## Pros / Cons & Notes 🔍

- **Inline script pros**: quick to write and run; minimal structure—good for throwaway scripts or simple demos.
- **Inline script cons**: hard to reuse, unit test, or integrate into larger projects; mixing I/O with logic reduces flexibility.
- **Function-based pros**: more modular, testable, and maintainable. A small change (e.g., returning a list) makes unit tests trivial.
- **Function-based cons**: slightly more boilerplate, but the tradeoff favors functions for maintainability.

---

## Suggested improvements (small, practical) 🔧

1. Change `print_fibonacci(n)` to return a list of integers (e.g., `def fibonacci(n) -> list[int]:`) and add a small wrapper that prints output — this makes testing straightforward.
2. Add type hints and a docstring to the function for clarity and static analysis.
3. Add unit tests (pytest) for boundary cases (n = 1, 2, larger n, invalid input).
4. Move input parsing / validation into its own function (or use argparse) for clearer CLI behavior.

---

## Example (recommended function signature)

```python
def fibonacci(n: int) -> list[int]:
    """Return first n Fibonacci numbers (n >= 1)."""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

Use a small `if __name__ == '__main__'` wrapper to parse input and print `" ".join(map(str, fibonacci(n)))`.

---

## Bottom line ✅
- For any script you may want to reuse, test, or evolve, prefer the **function-based** approach and make the function return data instead of printing directly.
- For throwaway demos, the inline approach is acceptable but scales poorly.

*Would you like me to refactor `fibonacci_function.py` to return a list and add a pytest test file?*