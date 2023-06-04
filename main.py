"""
Example usage demonstration script

Simple showcase of the three cipher classes implemented in this project
"""

from src.Abstract_Cipher import AbstractCipher
from src.Affine_Cipher import AffineCipher
from src.Caesar_Cipher import CaesarCipher
from src.RSA_System import RSA

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_cipher(cipher: AbstractCipher):
    """
    Runs the given cipher with some example input
    :param cipher: Any of `CaesarCipher`, `AffineCipher`, or `RSA`
    """
    message = "Super secretive message"
    ciphertext = cipher.encrypt(message)
    plaintext = cipher.decrypt(ciphertext)
    print('"' + message + '"' + " ->", cipher, "->", ciphertext)
    print('"' + plaintext + '"' + " <-", cipher, "<-", ciphertext)
    print()


if __name__ == '__main__':
    test_cipher(AffineCipher(5, 5))
    test_cipher(AffineCipher(7, 7))

    test_cipher(CaesarCipher(11))
    test_cipher(CaesarCipher(23))

    test_cipher(RSA(5, 7))
    test_cipher(RSA(13, 23))
