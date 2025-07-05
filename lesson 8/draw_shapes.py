# by Kami Bigdely
# Extract superclass.

class Shape:
    """
    Abstract base class for geometric shapes.
    Provides common functionality for all shape types including visibility control
    and display capabilities. This demonstrates the use of inheritance and polymorphism.
    """
    
    def __init__(self, x, y, visible=True):
        """
        Initialize a Shape with position and visibility settings.
        
        Args:
            x (float): X-coordinate of the shape's position
            y (float): Y-coordinate of the shape's position
            visible (bool): Whether the shape should be visible when drawn
        """
        self.x = x
        self.y = y
        self.visible = visible

    def display(self):
        """
        Display the shape if it's visible.
        Uses the class name to identify what type of shape is being drawn.
        """
        if self.visible:
            print(f'drew the {self.__class__.__name__.lower()}.')

    def set_visible(self, is_visible):
        """
        Set the visibility of the shape.
        
        Args:
            is_visible (bool): True to make shape visible, False to hide it
        """
        self.visible = is_visible

    def get_center(self):
        """
        Get the center point of the shape.
        This is an abstract method that must be implemented by subclasses.
        
        Raises:
            NotImplementedError: This method should be overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

class Circle(Shape):
    """
    Represents a circle shape with a radius.
    Inherits from Shape and implements circle-specific functionality.
    """
    
    def __init__(self, x, y, r, visible=True):
        """
        Initialize a Circle with center coordinates and radius.
        
        Args:
            x (float): X-coordinate of the circle's center
            y (float): Y-coordinate of the circle's center
            r (float): Radius of the circle
            visible (bool): Whether the circle should be visible when drawn
        """
        super().__init__(x, y, visible)
        self.r = r

    def get_center(self):
        """
        Get the center point of the circle.
        For a circle, the center is simply the (x, y) coordinates.
        
        Returns:
            tuple: (x, y) coordinates of the circle's center
        """
        return self.x, self.y

class Rectangle(Shape):
    """
    Represents a rectangle shape with width and height.
    Inherits from Shape and implements rectangle-specific functionality.
    """
    
    def __init__(self, x, y, width, height, visible=True):
        """
        Initialize a Rectangle with position, dimensions, and visibility.
        
        Args:
            x (float): X-coordinate of the rectangle's top-left corner
            y (float): Y-coordinate of the rectangle's top-left corner
            width (float): Width of the rectangle
            height (float): Height of the rectangle
            visible (bool): Whether the rectangle should be visible when drawn
        """
        super().__init__(x, y, visible)
        self.width = width
        self.height = height

    def get_center(self):
        """
        Get the center point of the rectangle.
        Calculates the center by adding half the width and height to the origin.
        
        Returns:
            tuple: (x, y) coordinates of the rectangle's center
        """
        return self.x + self.width / 2, self.y + self.height / 2

if __name__ == "__main__":
    # Create a circle and demonstrate visibility control
    circle = Circle(0, 0, 10, False)  # Create invisible circle
    circle.set_visible(True)          # Make it visible
    circle.display()                  # Draw the circle
    print('center point', circle.get_center())

    # Create a rectangle and demonstrate visibility control
    rect = Rectangle(10, 10, 20, 5)   # Create visible rectangle
    rect.set_visible(False)           # Hide the rectangle
    rect.display()                    # Does not display because it's hidden
    rect.set_visible(True)            # Make it visible again
    rect.display()                    # Now it displays
    print('center point', rect.get_center())
