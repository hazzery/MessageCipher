.. MessageCipher documentation master file, created by
   sphinx-quickstart on Tue Dec 12 19:07:34 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


MessageCipher
=============

Hello! Welcome to MessageCipher's documentation! This library was primarily
written as a learning excercise, aswell as a demonstration of my programming
habits.

To perform encryption and decryption with MessageCipher, simply import the main
class from one of the cipher modules:

 * :py:class:`message_cipher.rsa_system.RSA`
 * :py:class:`message_cipher.caesar_cipher.CaesarCipher`
 * :py:class:`message_cipher.affine_cipher.AffineCipher`

create an object, and use the :py:meth:`~message_cipher.encrypter.Encrypter.encrypt`
and :py:meth:`~message_cipher.decrypter.Decrypter.decrypt` methods available on
those objects. Like so:

.. code-block:: python

   from message_cipher.rsa_system import RSA

   rsa = RSA()

   ciphertext = rsa.encrypt("Plain text message")

   plaintext = rsa.decrypt(ciphertext)
   print(plaintext)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   _sources/message_cipher


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
