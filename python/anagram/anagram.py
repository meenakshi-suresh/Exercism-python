"""Provides functionality for finding anagrams in a list of candidate words."""
def find_anagrams(word, candidates):
    """
    Find anagrams of a given word from a list of candidate words.

    Args:
        word (str): The word to find anagrams for.
        candidates (list): A list of candidate words.
    Returns:
        list: A list of anagrams found in the candidates.
    """
    sorted_word = sorted(word.lower())
    return [w for w in candidates if sorted(w.lower()) == sorted_word and word.lower()!=w.lower()]
