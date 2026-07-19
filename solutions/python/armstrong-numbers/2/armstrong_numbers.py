"""Determine whether a number is an Armstrong number.

This module provides a function to check whether a given integer
is an Armstrong number by comparing the number with the sum of its
digits, where each digit is raised to the power of the total number
of digits.
"""
def is_armstrong_number(number):
    """Determine whether a number is an Armstrong number.

    Parameters:
        number (int): The integer to check.

    Returns:
        bool: True if the number is an Armstrong number,
        otherwise False.
    """
    num = number
    armstrong_sum = 0
    number_length = len(str(number))

    while num != 0:
        digit = num % 10
        armstrong_sum += digit ** number_length
        num = num // 10
    if armstrong_sum == number:
        return True
    return False
    