"""Calculate the score for a dart landing on a concentric dartboard."""
def score(x, y):
    """Return 0, 1, 5, or 10 based on the dart's distance from the origin."""

    if (x * x) + (y * y) <= 1:
        return 10

    if (x * x) + (y * y) <= 25:
        return 5

    if (x * x) + (y * y) <= 100:
        return 1

    return 0
