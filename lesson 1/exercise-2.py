"""
Exercise 2: Finding Three Consecutive Numbers

This exercise demonstrates a logic error in early return statements.
The goal is to check if a list contains three consecutive numbers that increase by 1.
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

# Expected Output: The program should return true if the list contains 3 consecutive numbers each increasing by 1.
# Actual Output: The code is returning false with the list [4, 1, 2, 3] when it should return true.
# Line Number Causing the Error: line 31.
# Cause of the Error: The code is stopping too early and returning false due to the else on line 27, it can be fixed by removing the else statement and returning false after the for loop.

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# Code is stopping to early and returning false due to the else on line 27, it can be fixed by removing the else statement and returning false after the for loop.

def contains_3_consecutive(list_of_nums):
    """
    Return True if the list contains 3 consecutive numbers each increasing by 1.
    
    Args:
        list_of_nums: A list of numbers to check
        
    Returns:
        True if there are 3 consecutive numbers increasing by 1, False otherwise
        
    Example:
        contains_3_consecutive([1, 2, 4]) should return False
        contains_3_consecutive([4, 1, 2, 3]) should return True (because 1,2,3 are consecutive)
    """
    
    # Loop through all possible starting positions for a sequence of 3 numbers
    # We need to stop 2 positions before the end since we're checking 3 numbers at a time
    for i in range(len(list_of_nums) - 2):
        
        # Check if we have 3 consecutive numbers starting at position i
        # The numbers should be: list_of_nums[i], list_of_nums[i]+1, list_of_nums[i]+2
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else: # BUG: This else statement causes the function to return False immediately
              # after checking just the first position, even if there might be
              # consecutive numbers later in the list!
              # fix by removing else statement and returning false after for loop
            return False

    # If we've checked all positions and found no consecutive sequence, return False
    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    
    # Test case 1: No consecutive sequence
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    # Test case 2: Has consecutive sequence [1, 2, 3]
    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True, but currently prints False due to the bug!

# - Expected vs. Actual Output: The program should return true if the list contains 3 consecutive numbers each increasing by 1. The code is returning false with the list [4, 1, 2, 3] when it should return true.
# - Error Message: No error message.
# - Line Number Causing the Error: line 31.
# - Developer Assumptions: The developer assumes that else will continue the loop. The code is stopping too early and returning false due to the else on line 27, it can be fixed by removing the else statement and returning false after the for loop.