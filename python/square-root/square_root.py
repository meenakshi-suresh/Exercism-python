"""Compute the square root of a perfect square using binary search."""
def square_root(number):
    """Return the square root of a perfect square.

    Args:
        number (int): The perfect square whose square root is to be computed.

    Returns:
        int: The square root of the given perfect square.
    """
    low = 0
    high = number
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        if mid * mid < number:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans
