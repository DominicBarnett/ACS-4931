"""Exercise 7: Find the Bug(s)

This exercise teaches you how to:
- Debug a complex recursive function with multiple bugs
- Use all the debugging skills learned in previous exercises
- Form hypotheses about expected behavior vs actual behavior
- Systematically identify and fix multiple issues

Key Learning Points:
- Complex bugs often require multiple debugging techniques
- Form hypotheses about what should happen at each step
- Use the call stack to understand recursive function flow
- Watch expressions can help track complex state changes
- Sometimes there are multiple bugs that need to be fixed together
"""

def replace_substring(sentence, start_str, replace_str):
    # This function should replace all occurrences of 'start_str' with 'replace_str'
    # Example: replace_substring('an apple and a banana', 'an', 'foo')
    # Should return: 'foo apple food a bfoofooa'
    
    # Set a breakpoint here to start debugging
    # Base case
    if len(sentence) < len(start_str):
        return sentence
        # This handles cases where the remaining sentence is too short

    # Recursive case
    if sentence[:len(start_str)] == start_str:
        # We found a match at the beginning
        remainder_of_sentence = sentence[len(start_str):]
        return replace_str + replace_substring(remainder_of_sentence, start_str, replace_str)
    else:
        # No match at the beginning, keep the first character and recurse
        return sentence[0] + replace_substring(sentence[1:], start_str, replace_str)
    
    # BUGS TO FIND:
    # 1. There's a logic error in the recursive structure
    # 2. The function doesn't handle overlapping matches correctly
    # 3. There might be an infinite recursion issue
    #
    # Debugging strategy:
    # 1. Set breakpoints and step through the function
    # 2. Use watch expressions to track 'sentence', 'start_str', 'replace_str'
    # 3. Examine the call stack to see recursive calls
    # 4. Form hypotheses about what each recursive call should return
    # 5. Compare expected vs actual behavior


if __name__ == '__main__':
    sentence = 'okay, I guess programming is okay.'
    result = replace_substring(sentence, 'okay', 'fantastic')
    print(result) # Should print: 'fantastic, I guess programming is fantastic.'
    # 
    # Expected behavior:
    # 1. Find 'okay' at the beginning, replace with 'fantastic'
    # 2. Continue with remaining text: ', I guess programming is okay.'
    # 3. Find 'okay' at the end, replace with 'fantastic'
    # 4. Result: 'fantastic, I guess programming is fantastic.'
    #
    # Debugging tips:
    # 1. Use the call stack to see how the recursion unfolds
    # 2. Watch the 'sentence' parameter change with each recursive call
    # 3. Check if the base case is being reached correctly
    # 4. Verify that the string slicing is working as expected