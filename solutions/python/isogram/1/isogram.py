"""Determine whether a phrase is an isogram."""
def is_isogram(phrase):
    """Determine if a phrase is an isogram.

    :param phrase: the phrase to check
    :return: True if the phrase is an isogram, otherwise False
    """
    seen = set()

    for letter in phrase.lower():
        if not letter.isalpha():
            continue 
        if letter in seen:
            return False
            
        seen.add(letter)
    return True
    