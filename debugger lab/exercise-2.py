"""Exercise 2: Step Over, Step Into, Step Out

This exercise teaches you how to:
- Use Step Into to enter function calls and see their internal execution
- Use Step Over to execute function calls without entering them
- Use Step Out to complete the current function and return to the caller
- Navigate between different function scopes in the debugger

Key Learning Points:
- Step Into: Goes into function calls to see their internal logic
- Step Over: Executes the current line without entering any function calls
- Step Out: Completes the current function and returns to where it was called
- The debugger won't step into library functions like len() by default
"""

def calculate_sum(list_of_nums):
    """Calculates the sum of a list of numbers."""
    total = 0
    # When you Step Into this function, you'll see:
    # - The 'list_of_nums' parameter with the passed values
    # - 'total' starting at 0 and accumulating the sum
    
    for num in list_of_nums:
        total += num
        # Step through this loop to see 'total' grow with each iteration

    return total
    # When you Step Out from here, you'll return to calculate_average()

def calculate_average(list_of_nums):
    """Calculates the average of a list of numbers."""
    # Set a breakpoint here to start debugging
    average = calculate_sum(list_of_nums) / len(list_of_nums)
    # Try these different approaches:
    # 1. Step Over: Will execute the entire calculate_sum() function at once
    # 2. Step Into: Will enter calculate_sum() to see its execution step by step
    # 3. Step Into, then Step Out: Will enter calculate_sum() but quickly return
    
    return average

if __name__ == '__main__':
    # Call calculate_average
    mylist = [2, 7, 3, 5, 11, 9]
    result = calculate_average(mylist)
    print(result)
    # Experiment with different stepping strategies:
    # - Step Over the calculate_average call to see the final result
    # - Step Into to explore the function's internal logic