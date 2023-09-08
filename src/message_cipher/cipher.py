"""
The cipher module defines the Cipher abstract base class.
"""
from abc import ABCMeta

from .encrypter import Encrypter
from .decrypter import Decrypter


class Cipher(Encrypter, Decrypter, metaclass=ABCMeta):
    """
    The Cipher class acts as an interface for objects that can both encrypt and decrypt messages.
    It allows for polymorphism between the different types of ciphers.
    """
