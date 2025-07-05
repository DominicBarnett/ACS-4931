# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, something):
    """
    Add an ingredient to the current mix and return the updated mix.
    
    Args:
        mix (list): Current list of ingredients
        something (str): Ingredient to add to the mix
    
    Returns:
        list: Updated mix with the new ingredient added
    """
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    """
    Simulates the process of mixing ice with cream to create a base.
    
    Returns:
        list: Base mixture of ice and cream
    """
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    """
    Create a customized drink based on the drink type and additional ingredients.
    
    This function demonstrates consolidating duplicate conditional fragments
    by extracting common operations into separate functions.
    
    Args:
        drink (str): Type of drink to make ('coffee' or 'strawberry milkshake')
        addons (list): Additional ingredients to add to the drink
    
    Returns:
        list: Complete list of ingredients in the final drink
    """
    mix = []
    
    # Handle coffee-based drinks
    if 'coffee' in drink:
        mix = add(mix, 'coffee')  # Start with coffee base
        # Add all additional ingredients to the coffee
        for addon in addons:
            mix = add(mix, addon)
    
    # Handle strawberry milkshake drinks
    elif 'strawberry milkshake' in drink:
        # Start with ice-cream base mixture
        mix = mixer_ice_with_cream()
        mix = add(mix, 'strawberry')  # Add strawberry flavor
        # Add all additional ingredients to the milkshake
        for addon in addons:
            mix = add(mix, addon)
    
    return mix

# Test the drink making system
# Create a strawberry milkshake with milk and sugar
final_drink = make_drink('strawberry milkshake', ['milk', 'sugar'])
print(final_drink)
