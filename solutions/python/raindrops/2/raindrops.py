"""Convert numbers into their corresponding raindrop sounds.

This module provides a function that converts an integer into a string
based on its factors. Numbers divisible by 3, 5, and 7 produce the
sounds "Pling", "Plang", and "Plong" respectively. If the number has
none of these factors, its string representation is returned.
"""
def convert(number):
    """Convert a number to its raindrop sound.

    Parameters:
        number (int): The number to convert.

    Returns:
        str: The raindrop sound corresponding to the number's factors,
        or the number as a string if it is not divisible by 3, 5, or 7.
    """
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if not result:
        result += str(number)

    return result