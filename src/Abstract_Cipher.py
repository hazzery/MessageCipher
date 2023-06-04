"""
Abstract Cipher module.

This module defines the AbstractCipher class,
which is a purely abstract base class (interface) for implementing various ciphers.
"""

from abc import ABCMeta, abstractmethod
from typing import Iterable


class AbstractCipher(metaclass=ABCMeta):
    """AbstractCipher acts as an interface for any cipher which can encrypt and decrypt messages."""

    @abstractmethod
    def encrypt(self, plaintext: str):
        """
        Encrypts a message using the cipher.
        :param plaintext: A message to be encrypted.
        :return: The encrypted message.
        """

        raise NotImplementedError

    @abstractmethod
    def decrypt(self, ciphertext: Iterable):
        """
        Decrypts an encrypted message using the cipher.
        :param ciphertext: An encrypted message to decrypt.
        :return: The decrypted message.
        """
        raise NotImplementedError
