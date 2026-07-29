"""Translate English words and phrases into Pig Latin."""
# pylint: disable=inconsistent-return-statements

def translate(text):
    """Return the Pig Latin translation of a word or phrase.

    Args:
        text (str): A word or phrase to translate.

    Returns:
        str: The Pig Latin translation.
    """

    vowels = ("a", "e", "i", "o", "u")

    def translate_word(word):
        """Return the Pig Latin translation of a single word."""

        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        for index, letter in enumerate(word):
            if word[index:index + 2] == "qu":
                return word[index + 2:] + word[:index + 2] + "ay"

            if letter in vowels or (letter == "y" and index > 0):
                return word[index:] + word[:index] + "ay"

    return " ".join(translate_word(word) for word in text.split())
