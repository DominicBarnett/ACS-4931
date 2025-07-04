"""Exercise 5: Stop on Exception

This exercise teaches you how to:
- Use the debugger to automatically stop when exceptions occur
- Examine variables at the point of failure to identify bugs
- Understand how to fix logic errors in algorithms
- Use debugging to understand algorithm behavior

Key Learning Points:
- The debugger automatically stops on uncaught exceptions
- Variables panel shows the state when the error occurred
- Use this information to identify what went wrong
- Fix the bug and verify the solution works
"""

def swap(lst, i, j):
    """Swap 2 items of a list in-place."""
    lst[i], lst[j] = lst[j], lst[i]

def bubble_sort(list_of_nums):
    """Sorts the list in-place using the Bubble Sort algorithm."""
    # BUG: This implementation has an index out of range error
    # The issue is in the nested loop structure
    
    for iteration in range(len(list_of_nums)): # Do n times
        for i in range(len(list_of_nums) - 1):
            if list_of_nums[i] > list_of_nums[i+1]:
                swap(list_of_nums, i, i+1)
    # When the exception occurs, examine:
    # - The values of 'iteration' and 'i'
    # - The current state of 'list_of_nums'
    # - The length of 'list_of_nums'
    # 
    # HINT: Think about what happens when 'i' reaches the end of the list
    # and we try to access 'list_of_nums[i+1]'


if __name__ == '__main__':
    nums = [12, 6, 2, 4, 3, 7]
    bubble_sort(nums)
    print(nums)
    # Expected output: [2, 3, 4, 6, 7, 12]
    # 
    # To fix the bug:
    # 1. Run the debugger without setting a breakpoint
    # 2. When it stops on the exception, examine the variables
    # 3. Identify why the index is out of range
    # 4. Fix the loop condition to prevent accessing beyond the list bounds