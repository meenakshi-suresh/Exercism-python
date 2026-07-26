"""Calculate resistor labels."""

COLOR_CODES = {
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

TOLERANCE_CODES = {
    "brown": "±1%",
    "red": "±2%",
    "green": "±0.5%",
    "blue": "±0.25%",
    "violet": "±0.1%",
    "grey": "±0.05%",
    "gold": "±5%",
    "silver": "±10%",
}


def resistor_label(colors):
    """Return the resistor label."""
    value = 0
    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        first, second, multiplier, tolerance = colors

        value = (
            (COLOR_CODES[first] * 10 + COLOR_CODES[second])
            * (10 ** COLOR_CODES[multiplier])
        )
        tolerance = TOLERANCE_CODES[tolerance]

    elif len(colors) == 5:
        first, second, third, multiplier, tolerance = colors

        value = (
            (
                COLOR_CODES[first] * 100
                + COLOR_CODES[second] * 10
                + COLOR_CODES[third]
            )
            * (10 ** COLOR_CODES[multiplier])
        )
        tolerance = TOLERANCE_CODES[tolerance]

    if value >= 1_000_000_000:
        value /= 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        value /= 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value /= 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    if value == int(value):
        value = int(value)

    return f"{value} {unit} {tolerance}"
