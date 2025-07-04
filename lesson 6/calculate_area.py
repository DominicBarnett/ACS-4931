# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max_value(li):  # TODO: Rename this function to reflect what it's doing.
    """
    Find the maximum value in a list of numbers.
    
    Args:
        li: List of numbers to search through
        
    Returns:
        The maximum value found in the list
    """
    m = li[0]  # Initialize with the first element as the current maximum
    for value in li:  # Iterate through each value in the list
        if value > m:  # If current value is greater than current maximum
            m = value  # Update the maximum to the current value
    return m  # Return the final maximum value

# Test the get_max_value function with a sample list
li = [5, -1, 43, 32, 87, -100]  # Sample list with positive and negative numbers
print(get_max_value(li))  # Should print 87 (the maximum value)

############################
def split_sentence(sentence):  # TODO: Rename this function to reflect what it's doing.
    """
    Split a sentence into individual words.
    
    Args:
        sentence: A string containing words separated by spaces
        
    Returns:
        A list of words from the sentence
    """
    words = sentence[0:].split(' ')  # Split the sentence by spaces to get individual words
    return words  # Return the list of words

# Test the split_sentence function with a sample sentence
print(split_sentence("If you were a vegetable, you'd be a 'cute-cumber.'"))
