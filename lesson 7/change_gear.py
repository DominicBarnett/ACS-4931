# By Kami Bigdely-Shamloo
# Consolidate duplicate conditional fragments
# This program changes car's gear according to the car speed. Then it 
# displays the updated gear on the car's front panel.

def change_gear(str_gear):
    """
    Simulates the physical gear change mechanism in a car.
    
    Args:
        str_gear (str): The gear to change to ('R', '1', '2', '3', '4')
    """
    print("Gear changed to", str_gear)

def display_gear(str_gear): 
    """
    Displays the current gear on the car's dashboard/instrument panel.
    
    Args:
        str_gear (str): The gear to display
    """
    print("displayed gear:", str_gear)

def process_speed(speed):
    """
    Determines the appropriate gear based on vehicle speed and executes gear change.
    
    Gear selection logic:
    - Speed <= 0: Reverse gear (R)
    - 0 < Speed < 30: First gear (1)
    - 30 <= Speed < 50: Second gear (2) 
    - 50 <= Speed <= 90: Third gear (3)
    - Speed > 90: Fourth gear (4)
    
    Args:
        speed (float): Current vehicle speed
    """
    # Handle reverse gear (when speed is zero or negative)
    if speed <= 0:
        display_gear('R')
    else:
        # Determine appropriate forward gear based on speed ranges
        if 0 <= speed < 30:
            gear = '1'  # First gear for low speeds
        elif 30 <= speed < 50:
            gear = '2'  # Second gear for moderate speeds
        elif 50 <= speed <= 90:
            gear = '3'  # Third gear for higher speeds
        else:
            gear = '4'  # Fourth gear for very high speeds
        
        # Execute the gear change and update display
        change_gear(gear)
        display_gear(gear)

# Test the gear changing system with a speed of 40 km/h
if __name__ == "__main__":
    process_speed(40)
