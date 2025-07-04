# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

def calculate_distance_between_two_circles(xc1, yc1, xc2, yc2):
    """
    Calculate the Euclidean distance between two circle centers.
    
    Uses the distance formula: sqrt((x2-x1)² + (y2-y1)²)
    
    Args:
        xc1, yc1: Coordinates of first circle center
        xc2, yc2: Coordinates of second circle center
        
    Returns:
        float: Distance between the two circle centers
    """
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

def calculate_vector_length(xa, ya, xb, yb):
    """
    Calculate the length of a vector from point A to point B.
    
    Uses the same distance formula as circles, but represents
    the magnitude of a vector from point A to point B.
    
    Args:
        xa, ya: Coordinates of point A (vector start)
        xb, yb: Coordinates of point B (vector end)
        
    Returns:
        float: Length of the vector from A to B
    """
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

def main():
    """
    Main function demonstrating distance calculations with sample coordinates.
    """
    # Sample coordinates for two circle centers
    xc1 = 4
    yc1 = 4.25

    xc2 = 53
    yc2 = -5.35

    # Sample coordinates for vector endpoints
    xa = -36
    ya = 97

    xb = .34
    yb = .91

    # Calculate and display results
    print('distance between two circles:', calculate_distance_between_two_circles(xc1, yc1, xc2, yc2))
    print('Lengh of vector:', calculate_vector_length(xa, ya, xb, yb))

main()