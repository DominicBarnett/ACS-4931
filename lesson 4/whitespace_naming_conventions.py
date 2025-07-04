# By Kami Bigdely
# PEP8 - whitespaces and variable names.
# This file demonstrates proper Python naming conventions and whitespace usage
# It implements a pizza ordering system with different pizza types

class Pizza:
    """
    Represents a pizza with customizable ingredients.
    
    This class demonstrates proper Python naming conventions and
    provides factory methods for creating different pizza styles.
    """
    
    def __init__(self, bread_type, cheese_type, meat_type, toppings, size):
        """
        Initialize a new pizza with specified ingredients.
        
        Args:
            bread_type (str): Type of bread/crust for the pizza
            cheese_type (str): Type of cheese used
            meat_type (str): Type of meat topping
            toppings (list): List of additional toppings
            size (str): Size of the pizza (e.g., 'small', 'medium', 'large')
        """
        self.bread_type = bread_type
        self.cheese_type = cheese_type
        self.meat_type = meat_type
        self.toppings = toppings
        self.size = size

    @classmethod
    def create_chicago_pizza(cls, size):
        """
        Create a Chicago-style deep dish pizza.
        
        Chicago pizza is known for its deep-dish crust, thick cheese layer,
        and chunky tomato sauce on top.
        
        Args:
            size (str): Size of the pizza
            
        Returns:
            Pizza: A new Chicago-style pizza instance
        """
        # Define Chicago-style pizza ingredients
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat_type = 'Italian sausage'
        toppings = ['green bell pepper', 'mushroom', 'chunky tomato sauce', 'onion']
        
        # Create and return the pizza instance
        return cls(bread, cheese, meat_type, toppings, size)

    @classmethod
    def create_california_pizza(cls, meat_type, size):
        """
        Create a California-style thin crust pizza.
        
        California pizza is known for its thin crust and fresh,
        healthy toppings like vegetables and lean meats.
        
        Args:
            meat_type (str): Type of meat to use on the pizza
            size (str): Size of the pizza
            
        Returns:
            Pizza: A new California-style pizza instance
        """
        # Define California-style pizza ingredients
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings = ['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        
        # Create and return the pizza instance
        return cls(bread, cheese, meat_type, toppings, size)

    def print_info(self):
        """
        Display information about the pizza.
        
        Prints all the details of the pizza including bread type,
        cheese type, meat type, and toppings in a readable format.
        """
        print('Bread type is:', self.bread_type)
        print('Cheese type is:', self.cheese_type)
        print('Meat type is:', self.meat_type)
        print('Toppings are:', ', '.join(self.toppings))


# Example usage: Create and display a California-style pizza
# This demonstrates how to use the Pizza class with factory methods
my_pizza = Pizza.create_california_pizza('chicken', 'large')
my_pizza.print_info()
