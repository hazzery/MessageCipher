"""RSA Decryprtion module.

The RSA decryption module defines the RsaDecrypter class.
Uses the RSA decryption algorithm to decrypt messages
in the form of arrays of integers
encrypted with the RSA encryption algorithm.
"""

from .conversions import int_to_char
from .decrypter import Decrypter


# pylint: disable=locally-disabled, too-few-public-methods
class RsaDecrypter(Decrypter):
    """RSA Decryption.

    RsaDecrypter performs calculations to decrypt
    arrays of integers into string messages.
    """

    def __init__(self, product: int, private_key: int):
        """Initialize a new RSA decryption system with values ``product`` and ``private_key``.

        :param product: The product of two large prime numbers.
        :param private_key: The private key used for decryption.
        """
        self.product = product
        self.__private_key = private_key

    def _decrypt_num(self, num: int) -> str:
        """Decrypts a single character using the RSA system.

        :param num: An integer to be decrypted.
        :return: A string of length 1 containing the decrypted letter.
        """
        number = pow(num, self.__private_key, self.product)
        return int_to_char(number).upper()

    def decrypt(self, ciphertext: list[int]) -> str:  # type: ignore[override]
        """Decrypts the encrypted message using the RSA system.

        :param ciphertext: An encrypted message to decrypt.
            The message should be a list of integers,
            as per output of ``RsaEncrypter.encrypt``.
        :return: The decrypted message as a string.
        """
        plaintext = ""
        for num in ciphertext:
            plaintext += self._decrypt_num(num)
        return plaintext
