# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

def is_good_level(total_cholostrol, ldl, triglyceride):
    """
    Check if cholesterol levels are within healthy ranges.
    
    Healthy thresholds:
    - Total cholesterol: < 200 mg/dL
    - LDL (bad cholesterol): < 100 mg/dL  
    - Triglycerides: < 150 mg/dL
    
    Args:
        total_cholostrol (int): Total cholesterol level in mg/dL
        ldl (int): LDL cholesterol level in mg/dL
        triglyceride (int): Triglyceride level in mg/dL
    
    Returns:
        bool: True if all levels are healthy, False otherwise
    """
    return total_cholostrol < 200 and ldl < 100 and triglyceride < 150

def is_high_cholestrol(total_cholostrol, ldl, triglyceride):
    """
    Check if cholesterol levels are dangerously high.
    
    High risk thresholds:
    - Total cholesterol: > 240 mg/dL
    - LDL: > 160 mg/dL
    - Triglycerides: >= 200 mg/dL
    
    Args:
        total_cholostrol (int): Total cholesterol level in mg/dL
        ldl (int): LDL cholesterol level in mg/dL
        triglyceride (int): Triglyceride level in mg/dL
    
    Returns:
        bool: True if any level is dangerously high, False otherwise
    """
    return 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200

def is_borderline_to_moderately_elevated(total_cholostrol, ldl, triglyceride):
    """
    Check if cholesterol levels are borderline or moderately elevated.
    
    Borderline thresholds:
    - Total cholesterol: 200-240 mg/dL
    - LDL: 130-160 mg/dL
    - Triglycerides: 150-200 mg/dL
    
    Args:
        total_cholostrol (int): Total cholesterol level in mg/dL
        ldl (int): LDL cholesterol level in mg/dL
        triglyceride (int): Triglyceride level in mg/dL
    
    Returns:
        bool: True if levels are borderline elevated, False otherwise
    """
    return 200 < total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200

def print_good_level_message():
    """Display message for healthy cholesterol levels."""
    print('*** Good level of cholestrol ***')

def print_high_cholestrol_message():
    """
    Display warning message and medical recommendations for high cholesterol.
    Includes medication and dietary advice.
    """
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')

def print_borderline_to_moderately_elevated_message():
    """
    Display recommendations for borderline cholesterol levels.
    Provides detailed dietary guidance including TLC diet information.
    """
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')

# Sample cholesterol test results (in mg/dL)
total_cholostrol = 70  # Very low total cholesterol
ldl = 30              # Very low LDL
triglyceride = 120    # Normal triglyceride level

# Evaluate cholesterol levels and provide appropriate recommendations
if is_good_level(total_cholostrol, ldl, triglyceride):
    print_good_level_message()
elif is_high_cholestrol(total_cholostrol, ldl, triglyceride):
    print_high_cholestrol_message()
elif is_borderline_to_moderately_elevated(total_cholostrol, ldl, triglyceride):
    print_borderline_to_moderately_elevated_message()
else:
    print('Error: unhandled case.')
