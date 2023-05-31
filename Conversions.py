def char_to_int(char: str) -> int:
    """
    Converts single character to numerical value
    :param char: string of length 1 containing a letter
    :return: integer representation of `char`
    :raises TypeError: If `char` is not a single character (string of length 1)
    :raises ValueError: If `char` is not a lowercase english letter
    """
    number = ord(char.lower()) - ord('a')

    if not 0 <= number < 26:
        raise ValueError("char must be a lowercase english letter")

    return number


def int_to_char(number: int) -> str:
    """
    Converts an integer to a character
    :param number: the integer to convert
    :return: string of length 1 containing letter representation of `number`
    :raises ValueError: If `number` is not within the bounds [0, 26)
    """
    if not 0 <= number < 26:
        raise ValueError("number must be in the range [0, 26)")

    return chr(ord('a') + number)
