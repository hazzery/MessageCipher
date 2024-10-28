"""Caesar Cipher module.

This module defines the CaesarCipher class,
which is a concrete implementation of the Mod26Cipher class.
The CaesarCipher class uses the Caesar cipher algorithm for encryption and decryption.
"""

from .conversions import char_to_int, int_to_char
from .modulo26_cipher import Mod26Cipher


class CaesarCipher(Mod26Cipher):
    """Encrypy and decrypt alphabetic text using the Ceasar Cipher algorithm."""

    def __init__(self, shift: int) -> None:
        """Initialize a new Caesar cipher with shift of ``shift``.

        :param shift: The number of letters to shift the alphabet by.
        """
        if not 0 <= shift < Mod26Cipher.NUMBER_OF_LETTERS_IN_ALPHABET:
            raise ValueError("Caesar cipher shift must be in range `0 <= shift < 26`")

        self.shift = shift

    def __repr__(self) -> str:
        """Create a string representation of the cipher.

        :return: An unambiguous string representation of this cipher.
        """
        return f"CaesarCipher({self.shift})"

    def _encrypt_char(self, char: str) -> str:
        """Encrypts a single character using the caesar cipher.

        :param char: A string of length 1 containing the letter to be encrypted.
        :return: A string of length 1 containing the encrypted letter.
        """
        number = (char_to_int(char) + self.shift) % 26
        return int_to_char(number)

    def _decrypt_char(self, char: str) -> str:
        """Decrypts a single character using the caesar cipher.

        :param char: A string of length 1 containing the letter to be decrypted.
        :return: A string of length 1 containing the decrypted letter.
        """
        number = (char_to_int(char) - self.shift) % 26
        return int_to_char(number)
