# by Kami Bigdely
# Remove control flag

def find_food(food, fridge):
    """
    Search for a specific food item in a list of available foods.
    
    This function demonstrates removing control flags by using early returns
    instead of setting a flag variable and checking it later.
    
    Args:
        food (str): The food item to search for
        fridge (list): List of available food items
    
    Returns:
        str or None: The found food item if present, None if not found
    """
    # Iterate through each item in the fridge/food list
    for item in fridge:
        # Check if the target food is contained in the current item
        if food in item:
            return item  # Early return when food is found
    
    # Return None if food is not found in any item
    return None

# Test the food finding function
if __name__ == "__main__":
    # Define the food to search for and the available food list
    food = 'wesabi'
    food_list = ['onion', 'cucumber', 'Guacamole', 'kabob barg', 'wesabi']
    
    # Search for the food item
    found_item = find_food(food, food_list)
    
    # Display the result with appropriate message
    print(food, "Found: " + found_item if found_item != None else "not found")
