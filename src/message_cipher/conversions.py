"""Conversions module.

This module defines functions for converting between characters and integers.
"""

from .modulo26_cipher import Mod26Cipher


def char_to_int(char: str) -> int:
    """Convert a single character to its numerical value.

    :param char: A string of length 1 containing a letter.
    :return: An integer representation of ``char``.
    :raises TypeError: If ``char`` is not a single character (string of length 1).
    :raises ValueError: If ``char`` is not an english letter.
    """
    number = ord(char.lower()) - ord("a")

    if not 0 <= number < Mod26Cipher.NUMBER_OF_LETTERS_IN_ALPHABET:
        raise ValueError("char must be a lowercase english letter")

    return number


def int_to_char(number: int) -> str:
    """Convert an integer to its corresponding character.

    :param number: An integer to convert.
    :return: A string of length 1 containing letter representation of ``number``.
    :raises ValueError: If ``number`` is not within the bounds [0, 26).
    """
    if not 0 <= number < Mod26Cipher.NUMBER_OF_LETTERS_IN_ALPHABET:
        raise ValueError("number must be in the range [0, 26)")

    return chr(ord("a") + number)
