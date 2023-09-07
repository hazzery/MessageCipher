"""
Abstract encrypter module.

This module defines the Decrypter class,
which is a purely abstract base class (interface) for implementing various ciphers.
"""

from abc import ABCMeta, abstractmethod


# pylint: disable=locally-disabled, too-few-public-methods
class Encrypter(metaclass=ABCMeta):
    """Encrypter acts as an interface for any object capable of encrypting messages."""

    @abstractmethod
    def encrypt(self, plaintext: str):
        """
        Encrypts degree_one message using the cipher.
        :param plaintext: A message to be encrypted.
        :return: The encrypted message.
        """

        raise NotImplementedError
