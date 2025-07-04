# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_input_from_user():
    """
    Get grade inputs from the user for 5 students.
    Returns a list of integer grades.
    """
    grade_list = []

    n_student = 5  # Number of students to get grades for
    for _ in range(n_student):
        # Get grade input from user and convert to integer
        grade_list.append(int(input('Enter a number: ')))

    return grade_list

def calculate_grades(grade_list):
    """
    Calculate the mean and standard deviation of a list of grades.
    
    Args:
        grade_list: List of numeric grades
        
    Returns:
        tuple: (mean, standard_deviation)
    """
    # Calculate the mean (average) of all grades
    total = 0
    for grade in grade_list:
        total += grade
    mean = total / len(grade_list)
    
    # Calculate the population standard deviation
    sd = 0
    sum_of_sqrs = 0
    for grade in grade_list:
        # Sum of squared differences from mean
        sum_of_sqrs += (grade - mean) ** 2
    # Standard deviation = square root of (sum of squares / number of grades)
    sd = math.sqrt(sum_of_sqrs / len(grade_list))

    return mean, sd

def print_grade_statistics(mean, sd):
    """
    Print the calculated grade statistics in a formatted way.
    
    Args:
        mean: Average grade
        sd: Standard deviation of grades
    """
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def main():
    """
    Main function that orchestrates the grade calculation process.
    """
    # Get grades from user input
    grade_list = get_input_from_user()
    # Calculate statistics
    completed_calculations = calculate_grades(grade_list)
    # Display results
    print_grade_statistics(completed_calculations[0], completed_calculations[1])

main()
