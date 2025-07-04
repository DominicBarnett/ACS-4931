# By Kami Bigdely
# Split temp variable
# This program demonstrates saving user information to a database and calculating age

def save_into_db(info):
    """
    Simulates saving information to a database.
    In a real application, this would connect to an actual database.
    
    Args:
        info: The information to be saved to the database
    """
    print(f"{info} saved into database")

# Get user input for username and save it to database
username = input('Please enter your username: ')  # Prompt user for username
save_into_db(username)  # Save the username to the database

# Get user input for birth year and calculate age
birth_year_input = int(input('Please enter your birth year: '))  # Get birth year as integer
current_year = 2024  # Set the current year (this should be dynamic in production)
age = current_year - birth_year_input  # Calculate age by subtracting birth year from current year

# Display the calculated age to the user
print("You are", age, "years old.")
