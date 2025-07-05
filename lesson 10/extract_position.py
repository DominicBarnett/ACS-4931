def extract_position(line):
    """
    Extracts a numerical position value from a log line that contains 'x:' coordinate.
    
    This function is designed to parse log messages from systems that output position
    data in a specific format. It looks for the 'x:' pattern and extracts the
    numerical value that follows it.
    
    Args:
        line (str): A log line that may contain position information in format 'x:value'
    
    Returns:
        float: The extracted position value as a floating-point number
    
    Raises:
        ValueError: If the line is invalid, contains debug/error keywords, or has no position data
    
    Examples:
        >>> extract_position('|update| the positron location in the particle accelerator is x:21.432')
        21.432
        >>> extract_position('|error| numerical calculations could not converge.')
        ValueError: Invalid line
    """
    # Input validation: check for empty lines or lines containing debug/error keywords
    # These are considered invalid as they don't contain useful position data
    if not line or 'debug' in line or 'error' in line:
        raise ValueError("Invalid line")
    
    # Check if the line contains position data (look for 'x:' pattern)
    if 'x:' not in line:
        raise ValueError("No position found in line")
    
    # Extract the position value:
    # 1. Find the index where 'x:' starts and move 2 characters past it
    start_index = line.find('x:') + 2
    
    # 2. Extract everything after 'x:' and remove leading/trailing whitespace
    pos = line[start_index:].strip()
    
    # 3. Convert the extracted string to a float and return it
    return float(pos)

# Test cases to demonstrate the function's behavior
if __name__ == "__main__":
    # Test case 1: Error line (should raise ValueError)
    try:
        result1 = extract_position('|error| numerical calculations could not converge.')
        print(result1)
    except ValueError as e:
        print(e)  # Expected output: "Invalid line"

    # Test case 2: Valid position line (should extract 21.432)
    try:
        result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
        print(result2)  # Expected output: 21.432
    except ValueError as e:
        print(e)
