"""Abstract decrypter module.

This module defines the Decrypter class,
which is a purely abstract base class (interface) for implementing various ciphers.
"""

from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from typing import Any


# pylint: disable=locally-disabled, too-few-public-methods
class Decrypter(metaclass=ABCMeta):
    """Decrypter acts as an interface for any abject capable of decrypting encrypted messages."""

    @abstractmethod
    def decrypt(self, ciphertext: Iterable[Any]) -> str:
        """Decrypts an encrypted message.

        :param ciphertext: An encrypted message to decrypt.
        :return: The decrypted message.
        """
