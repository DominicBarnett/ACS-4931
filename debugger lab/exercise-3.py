"""Exercise 3: Set a Watch Expression

This exercise teaches you how to:
- Create watch expressions to monitor specific values or calculations
- Use watch expressions to track variables that change during execution
- Combine multiple variables in expressions to gain insights
- Understand how data structures evolve during program execution

Key Learning Points:
- Watch expressions can contain any valid Python expression using in-scope variables
- They update in real-time as you step through the code
- Useful for monitoring complex calculations or data structure states
- Can help identify when variables have unexpected values
"""

import re

def clean_sentence(sentence):
    """
    Change to lowercase and remove any characters that are not letters or 
    spaces.
    """
    return re.sub(r'[^\w\s]', '', sentence.lower())

def find_most_common_word(sentence):
    """Return the most common word in the sentence."""
    
    # Set a breakpoint here to start debugging
    # Change to lowercase and strip out punctuation
    sentence = clean_sentence(sentence)
    # After this line, observe the cleaned sentence in the Variables panel

    list_of_words = sentence.split()
    # Watch expression suggestion: len(list_of_words)
    # This will show you how many words are in the sentence
    
    word_to_count = dict()
    # Watch expression suggestion: word_to_count
    # This will show the dictionary as it gets populated

    # Create a histogram of the occurrence of all words
    for word in list_of_words:
        if word not in word_to_count:
            word_to_count[word] = 1
        else:
            word_to_count[word] += 1
        # Watch expression suggestion: word_to_count['fish']
        # This will show the current count of 'fish' as it changes
    
    most_common_word = ''
    highest_count = 0
    # Watch expression suggestion: f"Current best: {most_common_word} ({highest_count})"
    # This will show the current best word and its count

    # Find highest count in the histogram
    for word, count in word_to_count.items():
        if count > highest_count:
            most_common_word, highest_count = word, count
        # Step through this loop to see how the best word changes

    return most_common_word

if __name__ == '__main__':
    result = find_most_common_word(
        'One fish, two fish, red fish, blue fish')
    print("The most common word is: " + result)
    # Expected result: "fish" (appears 4 times)
    # 
    # Try these watch expressions:
    # 1. len(list_of_words) - should be 8
    # 2. word_to_count['fish'] - should eventually be 4
    # 3. word_to_count - see the entire dictionary
    # 4. f"Processing: {word}" - see which word is being processed