"""Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths."""
def equilateral(sides):
    """An equilateral triangle has all three sides the same length.
        Input: All sides of a triangle
        Output: True if its an equilateral triangle False otherwise"""
    a, b, c = sides

    return (
        a > 0 and
        b > 0 and
        c > 0 and
        a + b >= c and
        a + c >= b and
        b + c >= a and
        a == b == c
    )


def isosceles(sides):
    """An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.).
        Input: All sides of a triangle
        Output: True if its an isosceles triangle False otherwise"""
    
    a,b,c = sides

    return (
        a > 0 and
        b > 0 and
        c > 0 and
        a + b >= c and 
        b + c >= a and 
        a + c >= b and 
        (a == b or
        b == c or 
        a == c)
    )
    


def scalene(sides):
    """A scalene triangle has all sides of different lengths.
       Input: All sides of a triangle
       Output: True if its an isosceles triangle False otherwise
    """
    
    a, b, c = sides

    return (
        a > 0 and
        b > 0 and
        c > 0 and
        a + b >= c and
        a + c >= b and
        b + c >= a and
        a != b != c != a
    )
    
