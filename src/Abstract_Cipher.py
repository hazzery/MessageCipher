"""
Abstract Cipher module.

This module defines the AbstractCipher class, which is an abstract base class for implementing various ciphers.
"""

from abc import ABCMeta, abstractmethod
from typing import Iterable


class AbstractCipher(metaclass=ABCMeta):
    """AbstractCipher acts as an interface for any cipher which can encrypt and decrypt messages"""

    @abstractmethod
    def encrypt(self, plaintext: str):
        """
        Encrypts a message using the cipher
        :param plaintext: message to be encrypted
        :return: string of encrypted message
        """

        raise NotImplementedError

    @abstractmethod
    def decrypt(self, ciphertext: Iterable):
        """
        Decrypts encrypted message using the cipher
        :param ciphertext: encrypted message to decrypt
        :return: decrypted message
        """
        raise NotImplementedError
