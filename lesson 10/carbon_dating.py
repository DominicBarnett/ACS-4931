import math

# Carbon-14 dating constants
T_HALF = 5730  # Half-life of Carbon-14 in years
DECAY_CONSTANT = -0.693  # Natural logarithm of 0.5 (ln(0.5)) for decay calculation

# TODO: Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'.
    # - Does the function handle every possible input correctly?
    # - What if the input is zero or negative?
    # - Add the necessary logic to make sure the function handle every possible input properly. Then write a unit test against this special case.

def get_age_carbon_14_dating(carbon_14_ratio):
    """
    Calculates the age of a sample using Carbon-14 dating method.
    
    Carbon-14 dating works by measuring the ratio of Carbon-14 remaining in a sample
    compared to the amount that would be present in living tissue. As Carbon-14 decays
    over time, this ratio decreases exponentially.
    
    Args:
        carbon_14_ratio (float): The ratio of Carbon-14 remaining in the sample
                                compared to living tissue (0 < ratio < 1)
    
    Returns:
        float: The estimated age of the sample in years, rounded to 2 decimal places
    
    Raises:
        ValueError: If the carbon_14_ratio is not within the valid range (0, 1]
    
    Formula:
        Age = (ln(carbon_14_ratio) / decay_constant) * half_life
        where:
        - ln() is the natural logarithm
        - decay_constant = ln(0.5) = -0.693
        - half_life = 5730 years for Carbon-14
    
    Example:
        If carbon_14_ratio = 0.35, the sample is approximately 8680.34 years old
    """
    # Input validation: ensure the ratio is within valid range
    if carbon_14_ratio <= 0 or carbon_14_ratio > 1:
        raise ValueError("Carbon-14 ratio must be positive and within 0-1.")
    
    # Apply the carbon dating formula:
    # Age = ln(ratio) / decay_constant * half_life
    age = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
    
    # Return age rounded to 2 decimal places for practical precision
    return round(age, 2)
