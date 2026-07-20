"""Generate Bob's responses to conversational remarks.

This module provides a function that determines Bob's reply based on
whether a remark is silence, a question, yelling, a yelled question,
or any other statement.
"""
def response(hey_bob):
    """Return Bob's response to a remark.

    Parameters:
        hey_bob (str): The remark addressed to Bob.

    Returns:
        str: Bob's appropriate response based on the type of remark.
    """
    if hey_bob.strip().endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip().endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if not hey_bob.strip():
        return "Fine. Be that way!"
    return "Whatever."
