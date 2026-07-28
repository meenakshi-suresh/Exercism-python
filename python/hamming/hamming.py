"""Calculate the Hamming distance between two DNA strands."""
def distance(strand_a, strand_b):
    """Return the Hamming distance between two DNA strands.

    Args:
        strand_a: The first DNA strand.
        strand_b: The second DNA strand.

    Returns:
        The number of positions at which the two strands differ.

    Raises:
        ValueError: If the strands are not of equal length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    length = len(strand_a)
    count = 0
    for i in range(length):
        if strand_a[i] != strand_b[i]:
            count += 1
    return count
