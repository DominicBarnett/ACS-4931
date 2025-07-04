# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

# TODO: Use 'extract method' refactoring technique to improve this code.
# TODO: If required, use 'replace temp variable with query' technique to make it easier to extract methods.

class Employer:
    """
    Represents an employer who can receive information about top students.
    """
    def __init__(self, name):
        # Initialize employer with a name
        self.name = name

    def send(self, students):
        # Send student contact information to the employer
        print("Students' contact info were sent to", self.name + '.')

class Student:
    """
    Represents a student with GPA and name information.
    """
    def __init__(self, gpa, name):
        # Initialize student with GPA and name
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        # Return the student's GPA
        return self.gpa

    def send_congrat_email(self):
        # Send a congratulatory email to the student for graduation
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    """
    Represents a school that manages students and graduation processes.
    """
    def __init__(self, students) -> None:
        # Initialize school with a list of students
        self.students = students

    def process_graduation(self):
        # Main method to handle the entire graduation process
        self.print_graduated_students()
        self.send_congrat_emails()
        self.send_top_students_to_employers()

    def passed_students(self):
        # Return list of students who passed (GPA > 2.5)
        min_gpa = 2.5
        return [s for s in self.students if s.get_gpa() > min_gpa]

    def print_graduated_students(self):
        # Print the names of all students who graduated
        print('*** Student who graduated *** ')
        for s in self.passed_students():
            print(s.name)
        print('****************************')

    def send_congrat_emails(self):
        # Send congratulatory emails to all students who passed
        for s in self.passed_students():
            s.send_congrat_email()

    def top_10_percent_students(self):
        # Return the top 10% of students based on GPA
        passed_students = self.passed_students()
        # Sort students by GPA in descending order
        passed_students.sort(key=lambda s: s.get_gpa(), reverse=True)
        # Calculate index for top 10% (90th percentile)
        index = int(0.9 * len(passed_students))
        return passed_students[:index]

    def send_top_students_to_employers(self):
        # Send top 10% students' information to major employers
        top_10_percent = self.top_10_percent_students()
        # Create list of major employers
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        # Send student information to each employer
        for e in top_employers:
            e.send(top_10_percent)

# Create sample students with different GPAs
students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
# Create school instance and process graduation
school = School(students)
school.process_graduation()

