"""
Affine Cipher module.

This module defines the AffineCipher class,
which is a concrete implementation of the Mod26Cipher class.

The AffineCipher class uses the Affine cipher algorithm for encryption and decryption.
"""

from .Conversions import char_to_int, int_to_char
from .Modulo26_Cipher import Mod26Cipher


def inverse_modulo_26(number: int) -> int:
    """
    Calculates the multiplicative inverse of `number` modulo 26.
    :param number: A number to calculate the inverse of.
    :return: The multiplicative inverse of number.
    """
    return pow(number, -1, 26)


class AffineCipher(Mod26Cipher):
    """
    AffineCipher performs calculations to encrypt and decrypt strings of alphabetic characters
    using the Affine Cipher algorithm.
    """

    INVERTIBLE_ELEMENTS = [1, 5, 7, 11, 13, 19, 23]

    def __init__(self, a: int, b: int):
        """
        Initializes a new Affine cipher with coefficients `a` and `b`.
        :param a: The degree one coefficient of the Affine cipher.
        :param b: The degree zero coefficient of the Affine cipher.
        """
        if a not in AffineCipher.INVERTIBLE_ELEMENTS:
            raise ValueError("Affine cipher coefficient 'a' must be invertible modulo 26")

        if not 0 <= b < 26:
            raise ValueError("Affine cipher coefficient 'b' must be in range `0 <= b < 26`")

        self.a = a
        self.b = b

    def __repr__(self):
        """
        Creates a string representation of the cipher.
        :return: An unambiguous string representation of this cipher.
        """
        return f"AffineCipher({self.a}, {self.b})"

    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the affine cipher.
        :param char: A string of length 1 containing the letter to be encrypted.
        :return: A string of length 1 containing the encrypted letter.
        """
        number = (char_to_int(char) * self.a + self.b) % 26
        return int_to_char(number)

    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the affine cipher.
        :param char: A string of length 1 containing the letter to be decrypted.
        :return: A string of length 1 containing the decrypted letter.
        """
        number = ((char_to_int(char) - self.b) * inverse_modulo_26(self.b)) % 26
        return int_to_char(number)
