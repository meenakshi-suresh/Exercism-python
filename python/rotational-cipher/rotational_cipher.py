"""Implement a rotational (Caesar) cipher.

This module provides a function to encrypt text by rotating each
alphabetic character by a specified number of positions while
preserving the original letter case. Non-alphabetic characters
remain unchanged.
"""
def rotate(text,key):
    """Encrypts the input text using a rotational cipher.
    Return: 
        str: The encrypted text after applying the rotational cipher.
    
    Args:
        text (str): The input text to be encrypted.
        key (int): The number of positions to rotate each alphabetic character.
    """
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = lowercase.upper()
    rotated_lowercase = lowercase[key:] + lowercase[:key]
    rotated_uppercase = uppercase[key:] + uppercase[:key]
    translation_table = str.maketrans(lowercase+uppercase, rotated_lowercase+rotated_uppercase)
    return text.translate(translation_table)
