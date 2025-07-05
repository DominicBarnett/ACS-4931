# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace nested conditional with guard clauses.

# Adjustment factor used in the capital calculation (30% reduction)
ADJ_FACTOR = 0.7

def get_adjusted_capital(capital, rate, duration, income):
    """
    Calculate the adjusted capital based on financial parameters.
    
    This function uses guard clauses to handle invalid inputs early,
    making the code more readable and maintainable.
    
    Args:
        capital (float): Initial capital amount
        rate (float): Interest rate
        duration (float): Time period
        income (float): Income amount
    
    Returns:
        float: Adjusted capital amount, or 0 if inputs are invalid
    """
    # Guard clause: Check if capital is negative or zero
    if capital <= 0:
        return 0
    
    # Guard clause: Check if rate or duration is invalid
    if rate <= 0 or duration <= 0:
        return 0
    
    # Calculate adjusted capital: (income/duration) * adjustment factor
    # This represents the income per time period, adjusted by the factor
    return (income / duration) * ADJ_FACTOR

# Example usage: Calculate adjusted capital for given parameters
# Capital: $50,000, Rate: 4%, Duration: 10 years, Income: $10,000
adjusted_capital = get_adjusted_capital(50000, 4, 10, 10000)
print(adjusted_capital)
