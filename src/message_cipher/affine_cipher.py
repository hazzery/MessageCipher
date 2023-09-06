"""
Affine Cipher module.

This module defines the AffineCipher class,
which is a concrete implementation of the Mod26Cipher class.

The AffineCipher class uses the Affine cipher algorithm for encryption and decryption.
"""

from .conversions import char_to_int, int_to_char
from .modulo26_cipher import Mod26Cipher


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

    INVERTIBLE_ELEMENTS = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    def __init__(self, degree_one: int, degree_zero: int):
        """
        Initializes a new Affine cipher with coefficients `degree_one` and `degree_zero`.
        :param degree_one: The polynomial degree one coefficient of the Affine cipher.
        :param degree_zero: The polynomial degree zero coefficient of the Affine cipher.
        """
        if degree_one not in AffineCipher.INVERTIBLE_ELEMENTS:
            raise ValueError("Affine cipher coefficient 'degree_one' must be invertible modulo 26")

        if not 0 <= degree_zero < 26:
            raise ValueError("Affine cipher coefficient 'degree_zero'\
                            must be in range `0 <= degree_zero < 26`")

        self.degree_one = degree_one
        self.degree_zero = degree_zero

    def __repr__(self):
        """
        Creates a string representation of the cipher.
        :return: An unambiguous string representation of this cipher.
        """
        return f"AffineCipher({self.degree_one}, {self.degree_zero})"

    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the affine cipher.
        :param char: A string of length 1 containing the letter to be encrypted.
        :return: A string of length 1 containing the encrypted letter.
        """
        number = (char_to_int(char) * self.degree_one + self.degree_zero) % 26
        return int_to_char(number)

    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the affine cipher.
        :param char: A string of length 1 containing the letter to be decrypted.
        :return: A string of length 1 containing the decrypted letter.
        """
        number = ((char_to_int(char) - self.degree_zero) * inverse_modulo_26(self.degree_one)) % 26
        return int_to_char(number)
