# Write a single-line comment and a multi-line docstring.

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The distance from the center to the edge.
        
    Returns:
        float: The total area calculated as pi * r^2.
    """
    import math
    return math.pi * (radius ** 2)

# Accessing documentation at runtime
print(calculate_area.__doc__)