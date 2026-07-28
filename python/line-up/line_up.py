"""Convert integers to their ordinal string representation."""
def line_up(name, number):
    """Return the ordinal representation of an integer.

    Args:
        number: The integer to convert.

    Returns:
        A string containing the number with its ordinal suffix.
    """
    number_suffix = {
        0: "th",
        1: "st",
        2: "nd",
        3: "rd"
    }
    if 10 < number%100 <= 20:
        suffix = "th"
    else:
        suffix = number_suffix.get(number%10,"th")
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
