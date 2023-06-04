"""
RSA Crypto System module.

This module defines functions for implementing the RSA encryption and decryption algorithm.
"""

from .Conversions import char_to_int, int_to_char
from .Abstract_Cipher import AbstractCipher
import random
import math


def is_prime(number: int) -> bool:
    """
    Checks all possible factors of `number` up to `sqrt(number)`
    to determine its primality
    :param number: number to check primality of
    :return: `True` if number is prime, otherwise `False`
    """
    # code from https://www.programiz.com/python-programming/examples/prime-number

    # prime numbers are greater than 1
    if number <= 1:
        return False

    composite = False
    # check for factors
    for i in range(2, int(math.sqrt(number) + 1)):
        if (number % i) == 0:
            # if factor is found, set flag to True
            composite = True
            break
    return not composite


def invertible_elements(number: int) -> list:
    """
    Calculates all numbers invertible modulo `number`
    :param number: The modulo to find invertible numbers in
    :return: list of all invertible elements
    """
    result = []
    for i in range(number):
        try:
            inverse = pow(i, -1, number)
            result.append(inverse)
        except ValueError:
            # `i` is not invertible modulo `number`
            # and should not be appended to list
            pass
    return result


class RSA(AbstractCipher):
    """
    RSA crypto-system class.
    Performs calculations to encrypt strings into an array of integers,
    and then decrypt those arrays back into strings

    This implements a simplified version of the RSA encryption algorithm
    """

    def __init__(self, p: int, q: int, e: int = None):
        """
        Initializes a new RSA system with values `p` and `q`
        :param p: First prime number for RSA system
        :param q: Second prime number for RSA system
        :param e: The exponent used for encryption (optional)
        :return: An `RSA` object for the given prime numbers
        """

        if not (is_prime(p) and is_prime(q)):
            raise ValueError("RSA system values `p` and `q` must be prime")

        self.n = p * q
        self.__phi_n = (p - 1) * (q - 1)

        if e is None:
            self.e = random.choice(invertible_elements(self.__phi_n))
        elif e in invertible_elements(self.__phi_n):
            self.e = e
        else:
            raise ValueError("Specified e value must be invertible modulo phi(n)")

        self.public_key = (self.n, self.e)

        self.__private_key = pow(self.e, -1, self.__phi_n)

    def __repr__(self):
        """
        String representation of `RSA` instance
        :return: String representing specified RSA system
        """
        return f"AffineCipher: {self.public_key}"

    def _encrypt_char(self, char: str) -> int:
        """
        Encrypts a single character using the affine cipher
        :param char: string of length 1 containing letter to be encrypted
        :return: string of length 1 containing encrypted letter
        """
        number = pow(char_to_int(char), self.e, self.n)
        return number

    def _decrypt_num(self, num: int) -> str:
        """
        Decrypts a single character using the affine cipher
        :param num: integer to be decrypted
        :return: string of length 1 containing decrypted letter
        """
        number = pow(num, self.__private_key, self.n)
        return int_to_char(number).upper()

    def encrypt(self, plaintext: str) -> list:
        """
        Encrypts a message using the cipher
        :param plaintext: message to be encrypted
        :return: string of encrypted message
        """

        ciphertext = []
        for char in plaintext:
            if char.isalpha():
                ciphertext.append(self._encrypt_char(char))
        return ciphertext

    def decrypt(self, cipher_array: list) -> str:
        """
        Decrypts encrypted message using the cipher
        :param cipher_array: encrypted message to decrypt,
            message should be a list of integers, as per output of encrypt function
        :return: string of decrypted message
        """
        plaintext = ""
        for num in cipher_array:
            plaintext += self._decrypt_num(num)
        return plaintext
