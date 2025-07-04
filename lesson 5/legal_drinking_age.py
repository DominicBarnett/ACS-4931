# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

# Legal age constant for drinking and night club entry
LEGAL_DRINKING_AGE = 18

class Person:
    """
    Represents a person with an age attribute.
    """
    def __init__(self, my_age):
        # Initialize person with their age
        self.age = my_age
        
def enter_night_club(individual):
    """
    Check if a person is old enough to enter a night club.
    
    Args:
        individual: Person object with age attribute
        
    Returns:
        None: Prints whether entry is allowed or denied
    """
    # Check if person meets the minimum age requirement
    if individual.age >= LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Entrance of minors is denied.")
    
# Create a person and test night club entry
person = Person(17.9)  # Person is under 18
enter_night_club(person)
        
