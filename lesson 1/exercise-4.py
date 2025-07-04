"""
Exercise 4: Binary Search Algorithm

This exercise demonstrates multiple issues in a binary search implementation:
1. Indentation error in docstring
2. Infinite recursion due to incorrect boundary updates
The goal is to find the index of an element in a sorted array using binary search.
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# Expected Output: The program is expected to perform a binary search on the sorted list [1, 2, 4, 5, 7] to find the index of the element 7. The expected output is the index 4.
# Actual Output: IndentationError: unindent does not match any outer indentation level and RecursionError: maximum recursion depth exceeded in comparison
# Line Number Causing the Error: line 28, 43, and 47
# Cause of the Error: The code likely contains a logical issue that prevents it from performing the binary search correctly.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

# The code assumes that the input list arr is sorted in ascending order. The code also assumes that the element is always in the list. Docscring is also indented incorrectly.

def binary_search(arr, element, low=0, high=None):
    """
    Returns the index of the given element within the array by performing a binary search.
    
    Binary search works by repeatedly dividing the search interval in half.
    If the value of the search key is less than the item in the middle of the interval,
    narrow the interval to the lower half. Otherwise narrow it to the upper half.
    
    Args:
        arr: A sorted list of numbers to search in
        element: The element to find
        low: The lower bound of the search range (default: 0)
        high: The upper bound of the search range (default: len(arr) - 1)
        
    Returns:
        The index of the element if found, -1 if not found
        
    Example:
        binary_search([1, 2, 4, 5, 7], 7) should return 4
    """ # BUG: Docstring is indented incorrectly - has an extra space
    
    # Initialize high to the last index if not provided
    if high == None:
        high = len(arr) - 1

    # Base case: if high < low, the element is not in the array
    if high < low:
        return -1

    # Calculate the middle index
    mid = (high + low) // 2

    # If we found the element, return its index
    if arr[mid] == element: 
        return mid

    # If the middle element is greater than the target, search the left half
    elif arr[mid] > element:
        # BUG: Should be mid - 1 to exclude the middle element from the search
        # Currently this can cause infinite recursion if the element is not found
        return binary_search(arr, element, low, mid) # should be return binary_search(arr, element, low, mid - 1)

    # If the middle element is less than the target, search the right half
    else: 
        # BUG: Should be mid + 1 to exclude the middle element from the search
        # Currently this can cause infinite recursion if the element is not found
        return binary_search(arr, element, mid, high) # should be return binary_search(arr, element, mid + 1, high)


if __name__ == '__main__':
    # Test the binary search with a sorted list
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)  # Should print 4, but crashes with indentation and recursion errors!

# - Expected vs. Actual Output: Expected to perform a binary search on the sorted list [1, 2, 4, 5, 7] to find the index of the element 7. The expected output is the index 4 but is returning an IndentationError and RecursionError.
# - Error Message: RecursionError: maximum recursion depth exceeded in comparison.
# - Line Number Causing the Error: lines 28, 43, and 47
# - Developer Assumptions: Docstring is one indent too far to the right. The recursion issue is because the developer doesn't account if the element is on the left or right side of the middle element. Should add a +1 or -1 to mid on the last 2 conditionals to fix this.