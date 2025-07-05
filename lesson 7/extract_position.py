# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):
    """
    Extract position value from a log line containing coordinate information.
    
    This function uses guard clauses to handle edge cases early:
    1. Empty or None lines
    2. Debug or error messages
    3. Lines without position data
    
    Args:
        line (str): Log line that may contain position data in format "x:value"
    
    Returns:
        str or None: The position value if found, None otherwise
    """
    # Guard clause: Check if line is empty or None
    if not line:
        return None
    
    # Guard clause: Skip debug and error messages
    if 'debug' in line or 'error' in line:
        return None
    
    # Check if the line contains position data (x: format)
    if 'x:' in line:
        # Extract the position value after "x:"
        start_index = line.find('x:') + 2  # Skip "x:" (2 characters)
        return line[start_index:]
    
    # No position data found
    return None

# Test the position extraction function
if __name__ == "__main__":
    # Test case 1: Error message (should return None)
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)  # output: None
    
    # Test case 2: Valid position data (should extract "21.432")
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)  # output: 21.432
