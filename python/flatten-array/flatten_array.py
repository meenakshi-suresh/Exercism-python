"""Flatten nested lists into a single list while ignoring None values."""
def flatten(iterable):
    """Return a flattened version of a nested list.

    Args:
        iterable: A list that may contain nested lists and None values.

    Returns:
        A new list containing all non-None elements in their original order.
    """
    result = []
    for item in iterable:
        if item is None:
            pass
        elif isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
