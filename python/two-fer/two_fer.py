"""Generate a two-fer phrase for a given name or a default recipient."""
def two_fer(name="you"):
    """Return the two-fer phrase for the given name.

    Args:
        name (str): The recipient's name. Defaults to "you".

    Returns:
        str: The formatted two-fer phrase.
    """
    return f"One for {name}, one for me."
