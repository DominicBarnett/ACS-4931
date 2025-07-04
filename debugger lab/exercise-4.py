"""Exercise 4: Use the Call Stack

This exercise teaches you how to:
- Navigate the call stack to see multiple function call contexts
- Understand how recursive functions build up and unwind the stack
- Examine variables in different stack frames
- See how parameters change across recursive calls

Key Learning Points:
- The call stack shows the history of function calls
- Each stack frame contains the variables and parameters for that function call
- Recursive functions create multiple stack frames with the same function
- You can click between stack frames to see different variable states
- The stack grows during recursive calls and shrinks during returns
"""

def fibonacci(n):
    """Calculates the fibonacci number of n."""
    # Set a breakpoint here to observe the call stack
    # Base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)
    # When you hit this line, observe:
    # - The call stack will grow as fibonacci() calls itself
    # - Each stack frame will have a different value of 'n'
    # - You can click between stack frames to see different 'n' values
    # - The stack will eventually unwind as base cases are reached


if __name__ == '__main__':
    result = fibonacci(6)
    print(result)
    # Expected result: 8 (fibonacci sequence: 0,1,1,2,3,5,8,13,...)
    #
    # Call stack progression for fibonacci(6):
    # 1. fibonacci(6) - calls fibonacci(5) + fibonacci(4)
    # 2. fibonacci(5) - calls fibonacci(4) + fibonacci(3)
    # 3. fibonacci(4) - calls fibonacci(3) + fibonacci(2)
    # 4. fibonacci(3) - calls fibonacci(2) + fibonacci(1)
    # 5. fibonacci(2) - calls fibonacci(1) + fibonacci(0)
    # 6. fibonacci(1) - returns 1 (base case)
    # 7. fibonacci(0) - returns 0 (base case)
    # Then the stack unwinds, calculating results back up