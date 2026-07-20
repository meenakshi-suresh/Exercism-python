"""Calculate the score for a dart landing on a concentric dartboard."""
def score(x, y):
    """Return 0, 1, 5, or 10 based on the dart's distance from the origin."""
    distance_squared = (x * x) + (y * y)
    
    if distance_squared <= 1:
        return 10

    if distance_squared <= 25:
        return 5

    if distance_squared <= 100:
        return 1

    return 0
