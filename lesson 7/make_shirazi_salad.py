# by Kami Bigdely
# Consolidate conditional expressions

def dice(ingredients):
    """
    Simulates the dicing/cutting process for salad ingredients.
    
    Args:
        ingredients (list): List of ingredients to be diced
    """
    print("diced all ingredients.")

def mix_all(diced_ingredients):
    """
    Simulates mixing all the diced ingredients together.
    
    Args:
        diced_ingredients (list): List of diced ingredients to mix
    """
    print("mixed all.")

def add_salt():
    """
    Simulates adding salt to the salad for seasoning.
    """
    print('added salt.')

def pour(liquid):
    """
    Simulates pouring a liquid ingredient into the salad.
    
    Args:
        liquid (str): The liquid ingredient to pour (e.g., lemon juice)
    """
    print('poured', liquid + '.')

def make_shirazi_salad(ingredients):
    """
    Make a traditional Iranian Shirazi salad with the provided ingredients.
    
    Shirazi salad is a refreshing Persian salad made with cucumber, tomato, 
    onion, and lemon juice. This function validates ingredients and follows
    the traditional preparation method.
    
    Args:
        ingredients (list): List of available ingredients
    
    Returns:
        None: Prints the preparation steps and final result
    """
    # Required ingredients for a proper Shirazi salad
    required_ingredients = ['cucumber', 'tomato', 'onion', 'lemon juice']
    
    # Check if all required ingredients are available
    # Uses 'all()' with generator expression to check each required ingredient
    if not all(ingredient in ingredients for ingredient in required_ingredients):
        print('lacks ingredients.')
        return
    
    # Follow the traditional Shirazi salad preparation steps
    dice(ingredients)           # Step 1: Dice all ingredients
    mix_all(ingredients)        # Step 2: Mix the diced ingredients
    add_salt()                  # Step 3: Add salt for seasoning
    pour('lemon juice')         # Step 4: Pour lemon juice for acidity
    print('Your yummy shirazi salad is ready!')

# Test the salad making function with all required ingredients
if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
