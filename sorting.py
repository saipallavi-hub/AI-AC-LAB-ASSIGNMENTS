#Generate Python code for QuickSort and BubbleSort, and include comments explaining step-by-step how each works and where they differ.
# QuickSort implementation
def quicksort(arr): 
    """
    QuickSort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array
    and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
    The sub-arrays are then sorted recursively.
    """
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively apply quicksort to left and right sub-arrays and combine results
    return quicksort(left) + middle + quicksort(right)
# BubbleSort implementation
def bubblesort(arr):
    """
    BubbleSort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    The process is repeated until the list is sorted.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Flag to check if any swapping occurred
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if they are in the wrong order
                swapped = True  # Set flag to True if a swap occurred
        # If no two elements were swapped in the inner loop, then the array is sorted
        if not swapped:
            break
    return arr
# Example usage:
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", sample_array)
    
    # Using QuickSort
    sorted_array_quick = quicksort(sample_array)
    print("Sorted array using QuickSort:", sorted_array_quick)
    
    # Using BubbleSort
    sorted_array_bubble = bubblesort(sample_array.copy())  # Use copy to avoid in-place sorting affecting original
    print("Sorted array using BubbleSort:", sorted_array_bubble)
# Differences:
# 1. QuickSort is generally faster and more efficient for large datasets due to its divide-and-conquer approach,
#    while BubbleSort has a time complexity of O(n^2) and is inefficient for large lists.
# 2. QuickSort is a recursive algorithm, whereas BubbleSort is iterative.               
# 3. QuickSort uses additional space for the sub-arrays, while BubbleSort sorts the array in place with O(1) additional space.

