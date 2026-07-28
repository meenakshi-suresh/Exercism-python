"""Calculate the square of sums, the sum of squares, and their difference."""
def square_of_sum(number):
    """Return the square of the sum of the first number natural numbers."""
    return (number * (number + 1) // 2) ** 2


def sum_of_squares(number):
    """Return the sum of the squares of the first number natural numbers."""
    total = 0
    for i in range(1,number+1):
        total += i ** 2
    return total


def difference_of_squares(number):
    """Return the difference between the square of the sum and the sum of the squares."""
    return (square_of_sum(number) - sum_of_squares(number))
