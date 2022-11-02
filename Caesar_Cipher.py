"""
Caesar Cipher
"""

from Conversions import *


class CaesarCipher:

    def __init__(self, shift: int):
        """
        Initializes a new Caesar cipher with shift of `shift`

        :param shift: The number of letters to shift the alphabet by
        :return: An `CaesarCipher` object for the given shift value
        """

        if not 0 <= shift < 26:
            raise ValueError("Caesar cipher shift must be in range `0 <= shift < 26`")

        self.shift = shift

    def __repr__(self):
        """
        String representation of `CaesarCipher` instance

        :return: String representing specified cipher
        """
        return f"CaesarCipher({self.shift})"

    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the caesar cipher

        :param char: string of length 1 containing letter to be encrypted
        :return: string of length 1 containing encrypted letter
        """
        number = (char_to_int(char) + self.shift) % 26
        return int_to_char(number)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the caesar cipher

        :param plaintext: message to be encrypted
        :return: string of encrypted message
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ciphertext += self._encrypt_char(char).upper()
        return ciphertext

    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the caesar cipher

        :param char: string of length 1 containing letter to be decrypted
        :return: string of length 1 containing decrypted letter
        """
        number = (char_to_int(char) - self.shift) % 26
        return int_to_char(number)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts encrypted message using the caesar cipher

        :param ciphertext: encrypted message to decrypt
        :return: string of decrypted message
        """
        plaintext = ""
        for char in ciphertext:
            plaintext += self._decrypt_char(char).upper()
        return plaintext
