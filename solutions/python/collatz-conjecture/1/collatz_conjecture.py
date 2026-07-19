"""Calculate the number of steps required to reach 1 using the Collatz process.

This module provides a function that computes the number of steps
needed for a positive integer to reach 1 by repeatedly applying the
Collatz rules.
"""
def steps(number):
    """Return the number of steps to reach 1 using the Collatz process.

    Parameters:
        number (int): A positive integer.

    Returns:
        int: The number of steps required for the number to reach 1.

    Raises:
        ValueError: If the number is not a positive integer.
    """
    number_of_steps = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        number_of_steps+=1
    return number_of_steps