"""Calculate the sum of unique multiples of given factors below a limit."""
def sum_of_multiples(limit, multiples):
    """Return the sum of unique multiples of the given factors below a limit.

    Args:
        limit (int): The exclusive upper limit.
        multiples (list[int]): The factors whose multiples are summed.

    Returns:
        int: The sum of all unique multiples less than the limit.
    """
    magical_set = set()
    for value in multiples:
        if value == 0:
            continue
        prod = value
        while prod < limit:
            magical_set.add(prod)
            prod += value
    return sum(magical_set)
