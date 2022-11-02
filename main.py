from Abstract_Cipher import AbstractCipher
from Affine_Cipher import AffineCipher
from Caesar_Cipher import CaesarCipher


def test_cipher(cipher: AbstractCipher):
    message = "Super secretive message"
    ciphertext = cipher.encrypt(message)
    plaintext = cipher.decrypt(ciphertext)
    print('"' + message + '"' + " ->", cipher, "-> " + ciphertext)
    print('"' + plaintext + '"' + " <-", cipher, "<- " + ciphertext)
    print()


if __name__ == '__main__':
    test_cipher(AffineCipher(5, 5))
    test_cipher(AffineCipher(7, 7))

    test_cipher(CaesarCipher(11))
    test_cipher(CaesarCipher(23))
