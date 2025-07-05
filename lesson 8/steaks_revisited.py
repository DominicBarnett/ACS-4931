# by Kami Bigdely
# Extract class

class SteakCooking:
    """
    Represents the cooking process for a steak with temperature, pressure, and time control.
    This class calculates cooking progress and determines when a steak has reached
    the desired doneness level (medium or well-done).
    """
    
    # Cooking thresholds for different doneness levels
    WELL_DONE = 3000  # Minimum cooking progress value for well-done steak
    MEDIUM = 2500     # Minimum cooking progress value for medium steak
    
    # Cooking constant that affects how cooking parameters combine
    COOKED_CONSTANT = 0.05

    def __init__(self, time, temperature, pressure, desired_state):
        """
        Initialize a steak cooking session with cooking parameters.
        
        Args:
            time (int): Cooking time in minutes
            temperature (int): Cooking temperature in Celsius
            pressure (int): Cooking pressure in PSI (Pounds per Square Inch)
            desired_state (str): Target doneness - 'medium' or 'well-done'
        """
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cookeding_criteria_satisfied(self):
        """
        Check if the steak has reached the desired cooking level.
        
        Returns:
            bool: True if steak meets the cooking criteria for desired doneness
        """
        return self.is_well_done() or self.is_medium()

    def is_well_done(self):
        """
        Check if the steak has reached well-done doneness.
        Requires both the desired state to be 'well-done' and sufficient cooking progress.
        
        Returns:
            bool: True if steak is well-done, False otherwise
        """
        return self.desired_state == 'well-done' and \
               self.get_cooking_progress() >= self.WELL_DONE

    def is_medium(self):
        """
        Check if the steak has reached medium doneness.
        Requires both the desired state to be 'medium' and sufficient cooking progress.
        
        Returns:
            bool: True if steak is medium, False otherwise
        """
        return self.desired_state == 'medium' and \
               self.get_cooking_progress() >= self.MEDIUM

    def get_cooking_progress(self):
        """
        Calculate the cooking progress based on time, temperature, pressure, and cooking constant.
        Higher values indicate more cooking has occurred.
        
        Returns:
            float: Cooking progress value (higher = more cooked)
        """
        return self.time * self.temperature * self.pressure * self.COOKED_CONSTANT


# Cooking parameters for the steak
time = 30  # Cooking time in minutes
temp = 103  # Cooking temperature in Celsius
pressure = 20  # Cooking pressure in PSI
desired_state = 'well-done'  # Target doneness level

# Create a steak cooking session with the specified parameters
steak_cooking = SteakCooking(time, temp, pressure, desired_state)

# Check if cooking is complete and provide feedback
if steak_cooking.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')
