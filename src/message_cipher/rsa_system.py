"""
RSA Crypto System module.

This module defines functions for implementing the RSA encryption and decryption algorithm.
"""

import math
import random
from typing import Iterator, Any

from .prime_generator import generate_large_prime
from .rsa_encrypter import RsaEncrypter
from .rsa_decrypter import RsaDecrypter
from .cipher import Cipher


def is_prime(number: int) -> bool:
    """
    Checks all possible factors of `number` up to `sqrt(number)`
    to determine its primality.
    :param number: A number to check the primality of.
    :return: `True` if number is prime, otherwise `False`.
    """
    # code from https://www.programiz.com/python-programming/examples/prime-number

    # prime numbers are greater than 1
    if number <= 1:
        return False

    composite = False
    # check for factors
    for i in range(2, int(math.sqrt(number) + 1)):
        if (number % i) == 0:
            # if a factor is found, set the flag to `True`
            composite = True
            break
    return not composite


def invertible_elements(number: int) -> list[int]:
    """
    Calculates all numbers invertible modulo `number`.
    :param number: The modulo to find invertible numbers in.
    :return: A list of all invertible elements.
    """
    result = []
    for i in range(number):
        try:
            inverse = pow(i, -1, number)
            result.append(inverse)
        except ValueError:
            # `i` is not invertible modulo `number`
            # and should not be appended to the list.
            pass
    return result


class RSA(Cipher, RsaEncrypter, RsaDecrypter):
    """
    RSA crypto-system constructor.
    Performs calculations to encrypt strings into an array of integers,
    and then decrypt those arrays back into strings.

    This implements a simplified version of the RSA encryption algorithm.
    """

    def __init__(self, prime1: int = 0, prime2: int = 0, exponent: int = 0):
        """
        Initializes a new RSA system with values `prime1` and `prime2`.
        :param prime1: First prime number for the RSA system.
        :param prime2: Second prime number for the RSA system.
        :param exponent: The exponent used for encryption (optional).
        """

        if prime2:
            if not (is_prime(prime1) and is_prime(prime2)):
                raise ValueError(
                    "RSA system values `prime1` and `prime2` must be prime"
                )
        else:
            prime1 = generate_large_prime()
            prime2 = generate_large_prime()

        product = prime1 * prime2
        __phi_n = (prime1 - 1) * (prime2 - 1)

        if not exponent:
            exponent = random.choice(invertible_elements(__phi_n))
        elif exponent not in invertible_elements(__phi_n):
            raise ValueError(
                "Specified exponent value must be invertible modulo phi(product)"
            )

        self.__private_key = pow(exponent, -1, __phi_n)

        RsaEncrypter.__init__(self, product, exponent)
        RsaDecrypter.__init__(self, product, self.__private_key)

    def __iter__(self) -> Iterator[Any]:
        """
        Returns an iterator for this RSA system.
        :return: An iterator for this RSA system.
        """
        return iter(
            (
                RsaEncrypter(self.product, self.exponent),
                RsaDecrypter(self.product, self.__private_key),
            )
        )
