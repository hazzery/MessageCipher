"""
Example usage demonstration script

Simple showcase of the three cipher classes implemented in this project
"""

from src.message_cipher.abstract_cipher import AbstractCipher
from src.message_cipher.affine_cipher import AffineCipher
from src.message_cipher.caesar_cipher import CaesarCipher
from src.message_cipher.rsa_system import RSA

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = ""


def test_cipher(cipher: AbstractCipher):
    """
    Runs the given cipher with some example input
    :param cipher: Any of `CaesarCipher`, `AffineCipher`, or `RSA`
    """
    ciphertext = cipher.encrypt(message)
    plaintext = cipher.decrypt(ciphertext)
    print('"' + message + '"' + " ->", cipher, "->", ciphertext)
    print('"' + str(ciphertext) + '"' + " ->", cipher, "->", plaintext)
    print()


if __name__ == '__main__':
    message = input("Enter a message to encrypt: ")
    test_cipher(AffineCipher(5, 13))
    test_cipher(AffineCipher(7, 19))

    test_cipher(CaesarCipher(11))
    test_cipher(CaesarCipher(23))

    test_cipher(RSA(5, 7))
    test_cipher(RSA(13, 23))
