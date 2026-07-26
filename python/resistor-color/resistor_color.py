"""Resistor color code mappings."""

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
    "white": 9,
}


def color_code(color):
    """Return the code for a color."""
    return colors_dict[color]


def colors():
    """Return the color names."""
    return list(colors_dict.keys())
