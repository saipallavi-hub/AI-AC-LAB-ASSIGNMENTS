#Task 3: Quick Sort and Merge Sort Comparison
#Implement Quick Sort and Merge Sort using recursion.
#Instructions: Provide AI with partially completed functions for recursion,Ask AI to complete the missing logic and add docstrings,Compare both algorithms on random, sorted, and reverse-sorted lists.
#Expected Output: Working Quick Sort and Merge Sort implementations,AI-generated explanation of average, best, and worst-case complexities.
# Quick Sort (recursive)
def quick_sort(arr):
    """Sorts list using Quick Sort algorithm"""
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Merge Sort (recursive)
def merge_sort(arr):
    """Sorts list using Merge Sort algorithm"""
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test cases
import random

data = [random.randint(1, 100) for _ in range(10)]

print("Original:", data)
print("Quick Sort:", quick_sort(data))
print("Merge Sort:", merge_sort(data))