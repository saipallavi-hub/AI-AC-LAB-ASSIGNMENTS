#Task 2: Implementing Bubble Sort with AI Comments
#Write a code in Python implementation of Bubble Sort.
#Instructions:Students implement Bubble Sort normally ,Ask AI to generate inline comments explaining key logic (like swapping, passes, and termination),Request AI to provide time complexity analysis.
#Expected Output:A Bubble Sort implementation with AI-generated explanatory comments and complexity analysis.
def bubble_sort(arr):
    n = len(arr)

    # Outer loop for number of passes
    for i in range(n):
        swapped = False  # To check if swapping happens

        # Inner loop for comparison
        for j in range(0, n - i - 1):

            # Swap if elements are in wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps happened, array is sorted
        if not swapped:
            break

    return arr


# Test
data = [64, 34, 25, 12, 22, 11, 90]
print("Sorted:", bubble_sort(data))