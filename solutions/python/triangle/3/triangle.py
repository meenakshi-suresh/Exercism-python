"""Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths."""
def equilateral(sides):
    """An equilateral triangle has all three sides the same length.
        Input: All sides of a triangle
        Output: True if its an equilateral triangle False otherwise"""
    side_a, side_b, side_c = sides

    return (
        all(side > 0 for side in sides) and
        side_a + side_b >= side_c and
        side_a + side_c >= side_b and
        side_b + side_c >= side_a and
        side_a == side_b == side_c
    )


def isosceles(sides):
    """An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.).
        Input: All sides of a triangle
        Output: True if its an isosceles triangle False otherwise"""
    
    side_a, side_b, side_c = sides

    return (
        all(side > 0 for side in sides) and
        side_a + side_b >= side_c and
        side_a + side_c >= side_b and
        side_b + side_c >= side_a and
        (side_a == side_b or
        side_b == side_c or 
        side_a == side_c)
    )
    


def scalene(sides):
    """A scalene triangle has all sides of different lengths.
       Input: All sides of a triangle
       Output: True if its an isosceles triangle False otherwise
    """
    
    side_a, side_b, side_c = sides

    return (
        all(side > 0 for side in sides) and
        side_a + side_b >= side_c and
        side_a + side_c >= side_b and
        side_b + side_c >= side_a and
        side_a != side_b != side_c != side_a
    )
    
