"""
Cipher
"""

from abc import *


class AbstractCipher(metaclass=ABCMeta):

    @abstractmethod
    def encrypt(self, plaintext: str):
        """
        Encrypts a message using the cipher
        :param plaintext: message to be encrypted
        :return: string of encrypted message
        """

        raise NotImplementedError

    @abstractmethod
    def decrypt(self, ciphertext):
        """
        Decrypts encrypted message using the cipher
        :param ciphertext: encrypted message to decrypt
        :return: decrypted message
        """
        raise NotImplementedError
