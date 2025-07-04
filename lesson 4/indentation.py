# by Kami Bigdely
# Indentation
# This file demonstrates proper indentation practices in Python
# It shows a simple person information management system

def write_to_db():
    """
    Writes person information to the database.
    
    This function handles the database write operation for storing
    person details. In a real application, this would include proper
    error handling and database connection management.
    """
    print('person info are written into db.')    
    
def set_person_info(first_name, last_name, gender, date_of_birth, photo, nationality, place_of_birth):
    """
    Validates and stores person information.
    
    This function validates the provided person information and then
    writes it to the database. It checks for required fields and
    provides feedback for missing information.
    
    Args:
        first_name (str): Person's first name
        last_name (str): Person's last name  
        gender (str): Person's gender
        date_of_birth (str): Person's date of birth
        photo (str): URL or path to person's photo
        nationality (str): Person's nationality
        place_of_birth (str): Person's place of birth
    """
    # Validate first name - check if it's empty or None
    if not first_name:
        print('first name is empty.') 
    
    # Validate last name - check if it's empty or None
    if not last_name:
        print('last name is empty.')
    
    # Additional validation could be added here for other fields
    # For example: gender validation, date format validation, etc.
    # ...    
    
    # Write the validated information to the database
    write_to_db()

# Example usage: Create a person record for Tim Hunt
# Photo URL points to Tim Hunt's Wikipedia page image
photo_path = "https://en.wikipedia.org/wiki/Tim_Hunt#/media/File:Tim_Hunt_at_UCSF_05_2009_(4).jpg"

# Call the function with Tim Hunt's information
# This demonstrates how to use the person information management system
set_person_info('Tim', 'Hunt', 'male','19 February 1943', photo_path, 'Uited Kingdom', 'Neston, Cheshire, England')