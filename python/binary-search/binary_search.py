"""Implement binary search for finding a value in a sorted list."""
def find(search_list, value):
    """Return the index of value in a sorted list using binary search.

    Args:
        search_list: A sorted list to search.
        value: The value to find.

    Returns:
        The index of value if it is present.

    Raises:
        ValueError: If value is not found in the list.
    """
    low = 0
    high = len(search_list)-1
    while low <= high:
        mid = (low+high) // 2
        if search_list[mid] == value:
            return mid
        if search_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError("value not in array")
