"""Classify numbers as perfect, abundant, or deficient."""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    perfect_sum = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    for num in range(1,number):
        if number % num == 0:
            perfect_sum += num

    if perfect_sum == number:
        return 'perfect'
    if perfect_sum < number:
        return 'deficient'
    if perfect_sum > number:
        return 'abundant'
        