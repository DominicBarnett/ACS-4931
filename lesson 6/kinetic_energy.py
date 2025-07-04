# By Kami Bigdely
# Remove assignment to method parameter.
# This program calculates kinetic energy using physics formulas with unit conversions

class Distance:
    """
    Represents a distance measurement with a value and unit.
    Used for storing distance data that may need unit conversion.
    """
    def __init__(self, value, unit):
        self.unit = unit  # Unit of measurement (e.g., 'km', 'ly' for light-years)
        self.value = value  # Numerical value of the distance

class Mass:
    """
    Represents a mass measurement with a value and unit.
    Used for storing mass data that may need unit conversion.
    """
    def __init__(self, value, unit):
        self.value = value  # Numerical value of the mass
        self.unit = unit  # Unit of measurement (e.g., 'kg', 'solar-mass')

def calculate_kinetic_energy(mass, distance, time):
    """
    Calculate kinetic energy using the formula: KE = 1/2 * mass * velocity^2
    where velocity = distance / time
    
    Args:
        mass: Mass object with value and unit
        distance: Distance object with value and unit  
        time: Time in seconds
        
    Returns:
        Kinetic energy in appropriate units, or None if unit conversion fails
    """
    # Extract values from the objects for calculations
    distance_value = distance.value
    mass_value = mass.value

    # Convert distance to kilometers if needed
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            # 1 light-year = 9.461 × 10^12 kilometers
            in_km = distance_value * 9.461e12
            distance = Distance(in_km, "km")
        else:
            print("unit is Unknown")
            return

    # Calculate speed (velocity) in km per second
    speed = distance_value / time  # [km per sec]
    
    # Convert mass to kilograms if needed
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            # 1 solar mass = 1.98892 × 10^30 kilograms
            mass_value *= 1.98892e30  # [kg]
            mass = Mass(mass_value, 'kg')
        else:
            print("unit is Unknown")
            return

    # Calculate kinetic energy using the formula: KE = 1/2 * m * v^2
    kinetic_energy = 0.5 * mass_value * speed ** 2
    return kinetic_energy

# Test the function with astronomical values
mass = Mass(2, "solar-mass")  # 2 solar masses
distance = Distance(2, 'ly')  # 2 light-years
print(calculate_kinetic_energy(mass, distance, 3600e20))  # Time in seconds

