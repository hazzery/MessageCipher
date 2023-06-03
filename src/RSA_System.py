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
    def __init__(self, p: int, q: int):
        """
        Initializes a new RSA system with values `p` and `q`
        :param p: first prime number for RSA system
        :param q: second prime number for RSA system
        :return: An `RSA` object for the given prime numbers
        """

        if not (is_prime(p) and is_prime(q)):
            raise ValueError("RSA system values `p` and `q` must be prime")

        self.p = p
        self.q = q

        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)

        self.e = random.choice(invertible_elements(self.phi_n))

        self.public_key = (self.n, self.e)

        self.private_key = pow(self.e, -1, self.phi_n)

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
        number = pow(num, self.private_key, self.n)
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

    def decrypt(self, ciphertext: list) -> str:
        """
        Decrypts encrypted message using the cipher
        :param ciphertext: encrypted message to decrypt
        :return: string of decrypted message
        """
        plaintext = ""
        for num in ciphertext:
            plaintext += self._decrypt_num(num)
        return plaintext
