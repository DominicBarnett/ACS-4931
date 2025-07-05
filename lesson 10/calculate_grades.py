# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.

import math

def display_grade_stat():
    """
    Main function that orchestrates the grade statistics calculation process.
    This function coordinates the entire workflow: reading input, calculating statistics,
    and displaying results.
    """
    # Step 1: Get grade data from user input
    grade_list = read_input()
    
    # Step 2: Calculate statistical measures (mean and standard deviation)
    mean, standard_deviation = calculate_stat(grade_list)
    
    # Step 3: Display the calculated statistics in a formatted output
    print_stat(mean, standard_deviation)

def read_input():
    """
    Collects grade inputs from the user with input validation.
    
    Returns:
        list: A list of integer grades entered by the user
        
    Note:
        - Prompts for exactly 5 student grades
        - Validates that each input is a valid integer
        - Continues prompting until valid input is received
    """
    grade_list = []
    n_student = 5  # Fixed number of students for this example
    
    # Loop through each student to collect their grade
    for _ in range(n_student):
        while True:
            try:
                # Prompt user for grade input
                grade = int(input('Enter a number: '))
                grade_list.append(grade)
                break  # Exit the while loop when valid input is received
            except ValueError:
                # Handle non-integer input gracefully
                print("Invalid input! Please enter an integer.")

    return grade_list

def calculate_stat(grade_list):
    """
    Calculates the mean and standard deviation of a list of grades.
    
    Args:
        grade_list (list): List of numeric grades
        
    Returns:
        tuple: (mean, standard_deviation) where both are float values
        
    Algorithm:
        1. Calculate mean: sum of all grades divided by number of grades
        2. Calculate standard deviation: square root of average squared differences from mean
    """
    # Calculate the mean (average) of all grades
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    
    # Calculate the standard deviation
    # Standard deviation measures how spread out the grades are from the mean
    sum_of_sqrs = 0
    for grade in grade_list:
        # For each grade, calculate its squared difference from the mean
        sum_of_sqrs += (grade - mean) ** 2
    
    # Standard deviation = square root of (average squared differences)
    sd = math.sqrt(sum_of_sqrs / len(grade_list))  # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """
    Displays the calculated statistics in a formatted, user-friendly output.
    
    Args:
        mean (float): The calculated mean of the grades
        sd (float): The calculated standard deviation of the grades
        
    Output:
        Prints formatted statistics with headers and rounded standard deviation
    """
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    # Round standard deviation to 3 decimal places for cleaner display
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

# Execute the main program when this script is run directly
if __name__ == "__main__":
    display_grade_stat()
