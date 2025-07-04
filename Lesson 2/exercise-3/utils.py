"""Utility functions for sorting and searching."""

# Merge Sort implementation

def merge_sort(arr):
    """Sort the list in-place using the merge sort algorithm."""
    if len(arr) <= 1:
        return # already sorted
    # Finding the midpoint of the array
    mid = len(arr) // 2

    # Dividing the array elements into 2 halves
    left_side = arr[:mid]
    right_side = arr[mid:]

    # Sorting the first and second half recursively
    merge_sort(left_side)
    merge_sort(right_side)

    i = j = k = 0

    # Merge the sorted halves back into the original array
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            arr[k] = left_side[i]
            i += 1
        else:
            arr[k] = right_side[j]
            j += 1
        k += 1

    # Copy any remaining elements from left_side
    while i < len(left_side):
        arr[k] = left_side[i]
        i += 1
        k += 1

    # Copy any remaining elements from right_side
    while j < len(right_side):
        arr[k] = right_side[j]
        j += 1
        k += 1

# Binary Search implementation

def binary_search(arr, elem):
    """Return the index of the given element within a sorted array, or -1 if not found."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        # Check if elem is present at mid
        if arr[mid] < elem:
            low = mid + 1

        # If elem is greater, ignore left half
        elif arr[mid] > elem:
            high = mid - 1

        # If elem is equal, return the index
        else:
            return mid

    # If we reach here, then the element was not present
    return -1
