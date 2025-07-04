# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)

# Constants for cooking criteria thresholds
WELL_DONE = 900000    # Minimum cooking value for well-done state
MEDIUM = 600000       # Minimum cooking value for medium state
COOKED_CONSTANT = 0.05  # Multiplier for cooking value calculation

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """
    Check if cooking criteria are satisfied based on time, temperature, pressure, and desired state.
    
    Uses the cooking value formula: time * temperature * pressure * COOKED_CONSTANT
    to determine if the food has been cooked to the desired level.
    
    Args:
        time: Cooking time
        temperature: Cooking temperature
        pressure: Cooking pressure
        desired_state: Target cooking state ('well-done' or 'medium')
        
    Returns:
        bool: True if cooking criteria are met, False otherwise
    """
    # Calculate cooking value using the formula
    cooking_value = time * temperature * pressure * COOKED_CONSTANT
    
    # Check if well-done criteria are met
    is_well_done = desired_state == 'well-done' and cooking_value >= WELL_DONE
    # Check if medium criteria are met
    is_medium = desired_state == 'medium' and cooking_value >= MEDIUM
    
    # Return True if either well-done or medium criteria are satisfied
    return is_well_done or is_medium

def main():
    """
    Main function demonstrating cooking criteria evaluation with sample values.
    """
    # Sample cooking parameters
    time = 30
    temp = 103
    pressure = 20
    desired_state = 'well-done'
    
    # Check if cooking is complete and display result
    if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
        print('cooking is done.')
    else:
        print('ongoing cooking.')

main()