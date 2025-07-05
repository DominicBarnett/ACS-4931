# by Kami Bigdely 
# Replace magic numbers with named constanst

# Physical constants for clarity and maintainability
COULOMBS_CONSTANT = 8.9875517923e9  # Coulomb's constant in N⋅m²/C²
EVEN_DIVISOR = 2  # Divisor used to determine if a number is even

def calculate_electric_force(q1, q2, distance):
    """
    Calculate the electric force exerted between two charges using Coulomb's Law.
    
    Coulomb's Law: F = k * (q1 * q2) / r²
    where k is Coulomb's constant, q1 and q2 are charges, and r is distance.
    
    Args:
        q1 (float): First charge in Coulombs
        q2 (float): Second charge in Coulombs  
        distance (float): Distance between charges in meters
    
    Returns:
        float: Electric force in Newtons
    """
    return COULOMBS_CONSTANT * q1 * q2 / (distance ** 2)

def is_even(number):
    """
    Check if a number is even by using modulo operation.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if number is even, False if odd
    """
    return number % EVEN_DIVISOR == 0

# Main program: Electric force calculation
print("=== Electric Force Calculator ===")
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))

# Calculate and display the electric force
force = calculate_electric_force(q1, q2, distance)
print("Electric Force between q1 and q2 is: ", force, "Newton")

# Main program: Even/Odd number checker
print("\n=== Even/Odd Number Checker ===")
num = int(input('Enter an integer number: '))
if is_even(num):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
