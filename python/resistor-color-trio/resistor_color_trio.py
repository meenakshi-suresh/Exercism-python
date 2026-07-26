"""Resistor Color Trio
Given the color bands of a resistor, return its value and label."""
def label(colors):
    """Return the label of the resistor.
    :param colors: list of color names
    :return: label of the resistor"""
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    first_digit = color_codes[colors[0]]
    second_digit = color_codes[colors[1]]
    multiplier = color_codes[colors[2]]

    resistance_value = (first_digit * 10 + second_digit) * (10 ** multiplier)
    if resistance_value >= 1000000000:
        return f"{resistance_value // 1000000000} gigaohms"
    if resistance_value >= 1000000:
        return f"{resistance_value // 1000000} megaohms"
    if resistance_value >= 1000:
        return f"{resistance_value // 1000} kiloohms"
    return f"{resistance_value} ohms"
