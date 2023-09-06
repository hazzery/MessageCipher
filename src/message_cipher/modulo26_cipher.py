"""
Modulo 26 Cipher module.

This module defines the Mod26Cipher class,
which is an abstract base class for implementing ciphers that operate on the modulo 26 alphabet.
"""

from abc import ABCMeta, abstractmethod
from .abstract_cipher import AbstractCipher


class Mod26Cipher(AbstractCipher, metaclass=ABCMeta):
    """
    Abstract Cipher class that operates exclusively on the english alphabet.
    Performs calculations to encrypt strings into an array of integers,
    and then decrypt those arrays back into strings.
    """

    @abstractmethod
    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the cipher.
        :param char: A string of length 1 containing the letter to be encrypted.
        :return: A string of length 1 containing the encrypted letter.
        """
        raise NotImplementedError

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the cipher.
        :param plaintext: A string message to be encrypted.
        :return: The encrypted message as a string.
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ciphertext += self._encrypt_char(char).upper()
        return ciphertext

    @abstractmethod
    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the cipher.
        :param char: A string of length 1 containing the letter to be decrypted.
        :return: A string of length 1 containing the decrypted letter.
        """
        raise NotImplementedError

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the encrypted message using the cipher.
        :param ciphertext: An encrypted message to decrypt.
        :return: The decrypted message as a string.
        """
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                plaintext += self._decrypt_char(char).upper()
        return plaintext
