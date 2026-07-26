""" Resistor Color Duo
Given the color bands of a resistor, return its value."""
def value(colors):
    """Return the value of the resistor.
    :param colors: list of color names
    :return: value of the resistor"""
    colors_dict = {
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
    return colors_dict[colors[0]] * 10 + colors_dict[colors[1]]
