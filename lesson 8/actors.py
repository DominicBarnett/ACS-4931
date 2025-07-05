# by Kami Bigdely
# Extract class

class Actor:
    """
    Represents an actor with personal information and movie history.
    This class manages actor data and provides functionality for hiring eligibility.
    """
    
    def __init__(self, first_name, last_name, birth_year, movies, email):
        """
        Initialize an Actor object with personal and professional information.
        
        Args:
            first_name (str): Actor's first name
            last_name (str): Actor's last name  
            birth_year (int): Year the actor was born
            movies (list): List of movies the actor has appeared in
            email (str): Actor's email address for contact
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def is_eligible_for_hiring(self):
        """
        Check if the actor is eligible for hiring based on birth year.
        Actors born after 1985 are considered eligible (younger generation).
        
        Returns:
            bool: True if actor is eligible (born after 1985), False otherwise
        """
        return self.birth_year > 1985

    def send_hiring_email(self):
        """
        Send a hiring email to the actor's email address.
        Currently prints a message to simulate email sending.
        """
        print("email sent to: ", self.email)

    def display_info_and_send_email(self):
        """
        Display actor information and send hiring email if eligible.
        This method combines displaying actor details and contacting them.
        """
        if self.is_eligible_for_hiring():
            # Display actor's full name
            print(f"{self.first_name} {self.last_name}")
            # Display all movies the actor has played in
            print('Movies Played: ', end='')
            for m in self.movies:
                print(m, end=', ')
            print()
            # Send hiring email to eligible actors
            self.send_hiring_email()

# Create a list of actor objects with sample data
actors = [
    Actor('elizabeth', 'debicki', 1990, ['Tenet', 'Vita & Virgina', 'Guardians of the Galaxy', 'The Great Gatsby'], 'deb@makeschool.com'),
    Actor('Jim', 'Carrey', 1962, ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man'], 'jim@makeschool.com')
]

# Process each actor: display info and send email if eligible
for actor in actors:
    actor.display_info_and_send_email()
