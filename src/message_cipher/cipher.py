"""The Cipher module defines the Cipher abstract base class."""

from abc import ABCMeta

from .decrypter import Decrypter
from .encrypter import Encrypter


# pylint: disable=locally-disabled, too-few-public-methods
class Cipher(Encrypter, Decrypter, metaclass=ABCMeta):
    """Cipher base class.

    Cipher is a combination of both an Encrypter and a Decrypter,
    and simply acts a common interface for objects
    capable of both encrypting plaintext,
    and decrypting messages encrypted using the corresponding encrypter
    """
