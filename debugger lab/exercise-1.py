"""Exercise 1: Step Through Code

This exercise teaches you how to:
- Set breakpoints to pause execution at specific lines
- Use Step Over to execute code line by line
- Observe variables changing in the Variables panel
- Understand how functions are called multiple times

Key Learning Points:
- Breakpoints stop execution before the marked line runs
- Step Over executes the current line and moves to the next
- Variables panel shows all in-scope variables and their current values
- The same breakpoint can be hit multiple times if the function is called multiple times
"""

def calculate_average(list_of_nums):
    """Calculates the average of a list of numbers."""
    total = 0       ### Set a breakpoint here! ###
    # When you hit this breakpoint, observe:
    # - The 'list_of_nums' variable in the Variables panel
    # - How 'total' starts at 0 and changes as you step through the loop
    # - The loop variable 'num' changing on each iteration
    
    for num in list_of_nums:
        total += num
        # Step through this line multiple times to see 'total' accumulate
        # and 'num' take on each value from the list

    average = total / len(list_of_nums)
    # At this point, 'total' should contain the sum of all numbers
    # and 'average' will be calculated
    
    return average

if __name__ == '__main__':
    # Call calculate_average
    mylist = [2, 7, 3, 5, 11, 9]
    result = calculate_average(mylist)
    print(result)
    # First time hitting the breakpoint: list_of_nums = [2, 7, 3, 5, 11, 9]

    # Call calculate_average a second time
    anotherlist = [-2, 5, -3]
    result2 = calculate_average(anotherlist)
    print(result2)
    # Second time hitting the breakpoint: list_of_nums = [-2, 5, -3]
    # Notice how the same breakpoint is hit twice with different data!