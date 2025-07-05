# Kami Bigdely
# Move Field

class Car:
    """
    Represents a car with various components including engine, wheels, cabin, and fuel tank.
    This class demonstrates a refactoring exercise to move TPMS (Tire Pressure Monitoring System)
    from the Car class to individual Wheel objects.
    """
    
    def __init__(self, engine, wheels, cabin, fuel_tank):
        """
        Initialize a Car object with its main components.
        
        Args:
            engine: The car's engine component
            wheels: List of Wheel objects for the car
            cabin: The car's cabin/interior component
            fuel_tank: The car's fuel storage component
        """
        self.engine = engine
        # TODO: tpms is better to be in the Wheel class. 
        # Each wheel has a single tpms attached to it. 
        # Thus, instead of having a list of tpms in 'Car' class
        # have each of the tpms in each 'Wheel'.
        self.tpms_list = tpms_di  # Tire Pressure Monitoring System.
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)
            
        self.cabin = cabin
        self.fuel_tank = fuel_tank

    
class Wheel:
    """
    Represents a car wheel with tire pressure monitoring capabilities.
    This class is designed to hold its own TPMS sensor for better encapsulation.
    """
    
    # TODO: You may add tpms as a method parameter here to 
    #       initilaize the 'Wheel' object or you can create
    #       a setter method to set the tpms of the wheel. (you can do 
    #       both of course.)
    def __init__(self, tpms, wheel_location = None, car = None):
        """
        Initialize a Wheel object with TPMS sensor and location information.
        
        Args:
            tpms: Tire Pressure Monitoring System sensor for this wheel
            wheel_location: Position of the wheel (e.g., 'front-right', 'back-left')
            car: Reference to the car this wheel belongs to
        """
        self.car = car
        self.wheel_location = wheel_location
        self.tpms = tpms

    def install_tire(self):
        """
        Simulate the process of installing a new tire on this wheel.
        Includes cleaning the TPMS sensor and installing new tube.
        """
        print('remove old tube.')
        # TODO: Rewrite the following after moving tpms to the 'Wheel' class
        print('cleaned tpms: ', self.tpms.get_serial_number(), '.')  # Use the wheel's own TPMS
        print('installed new tube.')        
        
    def read_tire_pressure(self):
        """
        Read the current tire pressure from this wheel's TPMS sensor.
        
        Returns:
            float: Current tire pressure reading
        """
        # TODO: After making tpms an attribute of 'Wheel' class,
        #       rewrite the following.
        return self.tpms.get_pressure()  # Use the wheel's own TPMS
    
    def set_car(self, car):
        """
        Set the reference to the car this wheel belongs to.
        
        Args:
            car: The Car object this wheel is attached to
        """
        self.car = car


class Tpms:
    """
    Tire Pressure Monitoring System.
    Represents a sensor that monitors tire pressure and provides pressure readings.
    """
    
    def __init__(self, serial_number):
        """
        Initialize a TPMS sensor with a unique serial number.
        
        Args:
            serial_number: Unique identifier for this TPMS sensor
        """
        self.serial_number = serial_number
        self.sensor_transmit_range = 300  # Transmission range in meters
        self.sensor_pressure_range = (8, 300)  # Pressure range in PSI (min, max)
        self.battery_life = 6  # Battery life in years
        
    def get_pressure(self):
        """
        Get the current tire pressure reading from the sensor.
        
        Returns:
            float: Current tire pressure in PSI
        """
        return 33
    
    def get_serial_number(self):
        """
        Get the unique serial number of this TPMS sensor.
        
        Returns:
            int: The sensor's serial number
        """
        return self.serial_number
    
class Engine:
    """
    Represents a car engine component.
    Placeholder class for engine functionality.
    """
    
    def __init__(self):
        pass
    
class FuelTank:
    """
    Represents a car's fuel storage tank.
    Placeholder class for fuel tank functionality.
    """
    
    def __init__(self):
        pass
    
class Cabin:
    """
    Represents a car's cabin/interior component.
    Placeholder class for cabin functionality.
    """
    
    def __init__(self):
        pass    

# Create car components
engine = Engine()
cabin  = Cabin()
fuel_tank = FuelTank()

# Create TPMS sensors for each wheel position
# Each wheel gets its own TPMS sensor with a unique serial number
tpms_di = {
    'front-right': Tpms(983408543), 
    'front-left': Tpms(4343083),
    'back-right': Tpms(23654835), 
    'back-left': Tpms(3498857)
}

# Create wheel objects, each with its own TPMS sensor
wheels = [
    Wheel(tpms_di['front-right'], 'front-right'), 
    Wheel(tpms_di['front-left'], 'front-left'),
    Wheel(tpms_di['back-right'], 'back-right'), 
    Wheel(tpms_di['back-left'], 'back-left')
]

# Create the complete car with all components
my_car = Car(engine, wheels, cabin, fuel_tank)
