from abc import ABCMeta

from .encrypter import Encrypter
from .decrypter import Decrypter


class Cipher(Encrypter, Decrypter, metaclass=ABCMeta):
    pass
