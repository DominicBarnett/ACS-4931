"""
Exercise 1: Finding the Largest Difference Between Consecutive Numbers

This exercise demonstrates a common off-by-one error in array indexing.
The goal is to find the largest absolute difference between consecutive numbers in a list.
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# Expected Output: The program should find and print the largest difference between consecutive numbers in the list [5, 3, 1, 2, 6, 4].
# Actual Output: The code is incomplete and will raise an error.
# Error Message: IndexError: list index out of range
# Line Number Causing the Error: line 31, in find_largest_diff diff = abs(list_of_nums[i] - list_of_nums[i+1])
# Cause of the Error: The code does not handle the last element of the list properly, which will result in an "IndexError" when trying to access list_of_nums[i+1] for the last element.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# The code assumes that the list always contains at least two elements for calculating the difference and should be changed to stop at the second to last index.

def find_largest_diff(list_of_nums):
    """
    Find the largest difference between *consecutive* numbers in a list.
    
    Args:
        list_of_nums: A list of numbers to analyze
        
    Returns:
        The largest absolute difference between any two consecutive numbers
        
    Example:
        find_largest_diff([5, 3, 1, 2, 6, 4]) should return 4
        (because the largest difference is between 2 and 6: |2-6| = 4)
    """
    largest_diff = 0
    
    # BUG: This loop goes through ALL elements, but we need to stop at the second-to-last
    # element because we're comparing each element with the next one (i+1)
    # When i reaches the last index, i+1 will be out of bounds!
    for i in range(len(list_of_nums)): # fix by stopping at second to last index with: for i in range(len(list_of_nums) - 1):
        
        # Calculate absolute difference between current element and next element
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        
        # Update largest_diff if we found a bigger difference
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    
    # Test the function with the example list
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    # But it will crash with IndexError instead!
    print(answer)

# - Expected vs. Actual Output: The program should find and print the largest difference between consecutive numbers in the list [5, 3, 1, 2, 6, 4]. The code is incomplete and will raise an error.
# - Error Message: IndexError: list index out of range
# - Line Number Causing the Error: line 31, in find_largest_diff diff = abs(list_of_nums[i] - list_of_nums[i+1])
# - Developer Assumptions: The code does not handle the last element of the list properly, which will result in an "IndexError" when trying to access list_of_nums[i+1] for the last element.