"""Determine whether a sentence is a pangram."""
def is_pangram(sentence):
    """Determine if a sentence contains every letter of the English alphabet.

    :param sentence: str the sentence to check
    :return: bool True if the sentence is a pangram, otherwise False
    """
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(sentence.lower())

    return alphabets.issubset(letters)
    
