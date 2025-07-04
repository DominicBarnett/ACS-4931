# by Kami Bigdely
# Docstrings and blank lines
# This file demonstrates proper use of docstrings and blank lines in Python code
# It implements a carbon monoxide detection system with temperature compensation

class OnBoardTemperatureSensor:
    """
    Represents an onboard temperature sensor.
    
    This class simulates a temperature sensor that reads voltage and converts it
    to temperature readings. In a real application, this would interface with
    actual hardware sensors.
    """
    # Conversion factor from voltage to temperature (volts to Celsius)
    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """
        Initializes the temperature sensor.
        
        In a real implementation, this would set up hardware connections
        and perform sensor calibration.
        """
        pass

    def read_voltage(self):
        """
        Reads the voltage from the sensor.
        
        Returns:
            float: The voltage reading from the sensor (in volts)
        """
        # Simulated voltage reading - in real hardware this would read from ADC
        return 2.7

    def get_temperature(self):
        """
        Calculates and returns the temperature in Celsius.
        
        Uses the voltage reading and conversion factor to determine temperature.
        
        Returns:
            float: Temperature in Celsius
        """
        # Convert voltage reading to temperature using the conversion factor
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
  
class CarbonMonoxideSensor:
    """
    Represents a carbon monoxide sensor.
    
    This class simulates a CO sensor that reads voltage and converts it to
    carbon monoxide levels, with temperature compensation for accuracy.
    """
    # Conversion factor from voltage to CO level (volts to ppm)
    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """
        Initializes the carbon monoxide sensor with a temperature sensor.
        
        Args:
            temperature_sensor: An OnBoardTemperatureSensor instance for temperature compensation
        """
        self.on_board_temp_sensor = temperature_sensor
        # Create a default temperature sensor if none provided
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """
        Calculates and returns the carbon monoxide level.
        
        Reads sensor voltage and applies temperature compensation to get accurate CO levels.
        
        Returns:
            float: Carbon monoxide level in parts per million (ppm)
        """
        # Read the raw voltage from the CO sensor
        sensor_voltage = self.read_sensor_voltage()
        # Convert voltage to CO level using temperature compensation
        self.carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """
        Reads the sensor voltage (placeholder for real hardware interaction).
        
        In a real implementation, this would read from an analog-to-digital converter
        connected to the CO sensor.
        
        Returns:
            float: Voltage reading from the CO sensor
        """
        # In real life, it should read from hardware.  
        return 2.3

    @staticmethod
    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """
        Converts voltage and temperature readings to a carbon monoxide level.
        
        This method applies temperature compensation to the voltage reading
        to provide accurate CO measurements.
        
        Args:
            voltage (float): Voltage reading from the sensor
            temperature (float): Temperature in Celsius for compensation
            
        Returns:
            float: Carbon monoxide level in parts per million (ppm)
        """
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature
    
class DisplayUnit:
    """
    Represents a display unit for showing sensor readings.
    
    This class handles the output of sensor data to the user interface.
    In a real application, this might interface with LCD displays, LEDs, or
    network communication for remote monitoring.
    """
    def __init__(self):
        """
        Initializes the display unit.
        
        Sets up the display for showing sensor readings and alerts.
        """
        self.string = ''

    def display(self, msg):
        """
        Displays a given message.
        
        Args:
            msg (str): The message to display
        """
        print(msg)

class CarbonMonoxideDevice:
    """
    Represents a carbon monoxide detection device.
    
    This is the main class that coordinates the CO sensor and display unit
    to create a complete carbon monoxide monitoring system.
    """
    def __init__(self, co_sensor, display_unit):
        """
        Initializes the device with a CO sensor and a display unit.
        
        Args:
            co_sensor: A CarbonMonoxideSensor instance
            display_unit: A DisplayUnit instance for output
        """
        self.carbon_monoxide_sensor = co_sensor 
        self.display_unit = display_unit       

    def display(self):
        """
        Displays the carbon monoxide level.
        
        Reads the current CO level from the sensor and displays it
        using the display unit.
        """
        # Get the current CO level and format it for display
        msg = 'Carbon Monoxide Level is: ' + str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

# Main execution block - demonstrates how to use the CO detection system
if __name__ == "__main__":
    # Create the sensor components
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    
    # Create the complete CO detection device
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    
    # Display the current CO level
    co_device.display()
