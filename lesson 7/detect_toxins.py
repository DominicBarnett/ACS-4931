# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    """
    Simulates an alert sound when toxins are detected in food.
    This would typically trigger a warning system in a food safety application.
    """
    print('made alert sound.')

def make_accept_sound():
    """
    Simulates an acceptance sound when food is confirmed toxin-free.
    This provides positive feedback for safe food items.
    """
    print('made acceptance sound')

def contains_toxin(ingredients):
    """
    Check if any toxic ingredients are present in the food ingredient list.
    
    Toxic ingredients monitored:
    - sodium nitrate: preservative that can form carcinogenic compounds
    - sodium benzoate: preservative that can react with vitamin C
    - sodium oxide: caustic compound that can cause burns
    
    Args:
        ingredients (list): List of food ingredients to check
    
    Returns:
        bool: True if any toxic ingredient is found, False otherwise
    """
    # List of known toxic ingredients to check for
    toxic_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
    
    # Check if any toxic ingredient is present in the food ingredients
    return any(toxin in ingredients for toxin in toxic_ingredients)

# Sample food ingredients to test
ingredients = ['sodium benzoate']

# Check for toxins and provide appropriate feedback
if contains_toxin(ingredients):
    # Display warning message with visual emphasis
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    # Display confirmation message for safe food
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
