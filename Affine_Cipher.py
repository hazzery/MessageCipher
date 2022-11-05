"""
Affine Cipher
"""
from Conversions import *
from Modulo26_Cipher import Mod26Cipher


def inverse_modulo_26(number: int) -> int:
    """
    Calculates the multiplicative inverse of `number` modulo 26
    :param number: number to calculate inverse of
    :return: the multiplicative inverse
    """
    return pow(number, -1, 26)


class AffineCipher(Mod26Cipher):

    INVERTIBLE_ELEMENTS = [1, 5, 7, 11, 13, 19, 23]

    def __init__(self, a: int, b: int):
        """
        Initializes a new Affine cipher with coefficients `a` and `b`
        :param a: The degree one coefficient of the Affine cipher
        :param b: The degree zero coefficient of the Affine cipher
        :return: An `AffineCipher` object for the given coefficients
        """
        if a not in AffineCipher.INVERTIBLE_ELEMENTS:
            raise ValueError("Affine cipher coefficient 'a' must be invertible modulo 26")

        if not 0 <= b < 26:
            raise ValueError("Affine cipher coefficient 'b' must be in range `0 <= b < 26`")

        self.a = a
        self.b = b

    def __repr__(self):
        """
        String representation of `AffineCipher` instance

        :return: String representing specified cipher
        """
        return f"AffineCipher({self.a}, {self.b})"

    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the affine cipher
        :param char: string of length 1 containing letter to be encrypted
        :return: string of length 1 containing encrypted letter
        """
        number = (char_to_int(char) * self.a + self.b) % 26
        return int_to_char(number)

    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the affine cipher
        :param char: string of length 1 containing letter to be decrypted
        :return: string of length 1 containing decrypted letter
        """
        number = ((char_to_int(char) - self.b) * inverse_modulo_26(self.b)) % 26
        return int_to_char(number)
