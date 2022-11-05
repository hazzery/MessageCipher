"""
Cipher
"""

from Abstract_Cipher import AbstractCipher


class Mod26Cipher(AbstractCipher):

    def _encrypt_char(self, char: str) -> str:
        """
        Encrypts a single character using the cipher
        :param char: string of length 1 containing letter to be encrypted
        :return: string of length 1 containing encrypted letter
        """
        raise NotImplementedError

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the cipher
        :param plaintext: message to be encrypted
        :return: string of encrypted message
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                ciphertext += self._encrypt_char(char).upper()
        return ciphertext

    def _decrypt_char(self, char: str) -> str:
        """
        Decrypts a single character using the cipher
        :param char: string of length 1 containing letter to be decrypted
        :return: string of length 1 containing decrypted letter
        """
        raise NotImplementedError

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts encrypted message using the cipher
        :param ciphertext: encrypted message to decrypt
        :return: string of decrypted message
        """
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                plaintext += self._decrypt_char(char).upper()
        return plaintext
