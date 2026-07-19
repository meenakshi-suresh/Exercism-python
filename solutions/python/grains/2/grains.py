"""Calculate the number of grains of wheat on a chessboard.

This module provides functions to calculate the number of grains
on an individual square and the total number of grains on all
64 squares of a chessboard.
"""
def square(number):
    """Return the number of grains on a given square.

    Parameters:
        number (int): The chessboard square number (1 to 64).

    Returns:
        int: The number of grains on the specified square.

    Raises:
        ValueError: If the square number is not between 1 and 64."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total number of grains on the chessboard.

    Returns:
        int: The total number of grains on all 64 squares.
    """
    total_grains = 0
    for num in range(1,65):
        total_grains += square(num)
    return total_grains
        