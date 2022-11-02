def char_to_int(char: str) -> int:
    """
    Converts single character to numerical value

    :param char: string of length 1 containing a letter
    :return: integer representation of `char`
    """
    number = ord(char.lower()) - ord('a')
    if not 0 <= number < 26:
        raise ValueError("char must be valid english letter")
    return number


def int_to_char(number: int) -> str:
    """
    Converts an integer to a character

    :param number: the integer to convert
    :return: string of length 1 containing letter representation of `number`
    """
    assert 0 <= number < 26
    return chr(ord('a') + number)