"""RSA Encryption module.

The RSA encryption module defines the RsaEncrypter class,
a concrete implementation of the Encrypter class.
Uses the RSA encryption algorithm to encrypt string messages into arrays of integers.
"""

from .conversions import char_to_int
from .encrypter import Encrypter


# pylint: disable=locally-disabled, too-few-public-methods
class RsaEncrypter(Encrypter):
    """RsaEncrypter performs calculations to encrypt string messages."""

    def __init__(self, product: int, exponent: int):
        """Initialise a new RSA decrypter with specified ``exponent`` and ``product``.

        :param product: The product of two large prime numbers.
        :param exponent: The exponent used for encryption.
        """
        self.exponent = exponent
        self.product = product

    def _encrypt_char(self, char: str) -> int:
        """Encrypts a single character using the RSA system.

        :param char: A string of length 1 containing the letter to be encrypted.
        :return: A string of length 1 containing the encrypted letter.
        """
        number = pow(char_to_int(char), self.exponent, self.product)
        return number

    def encrypt(self, plaintext: str) -> list[int]:
        """Encrypt a message using the RSA system.

        :param plaintext: A message to be encrypted.
        :return: The encrypted message as an array of integers.
        """
        cipher_array = []
        for char in plaintext:
            if char.isalpha():
                cipher_array.append(self._encrypt_char(char))
        return cipher_array
