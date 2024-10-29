"""Caesar Cipher unit testing suite."""

import unittest

from src.message_cipher.caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    """Rest suite to performs testing on all functionality relevant to the CaesarCipher class."""

    def test_invalid_coefficient(self) -> None:
        """Coefficients not in range [0, 26)."""
        self.assertRaises(ValueError, CaesarCipher, 26)
        self.assertRaises(ValueError, CaesarCipher, 100)
        self.assertRaises(ValueError, CaesarCipher, -1)
        self.assertRaises(ValueError, CaesarCipher, -100)

    def test_encrypt(self) -> None:
        """Tests basic string encryption, checking uppercase, lowercase, and white-space."""
        cipher = CaesarCipher(3)
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_ciphertext = "KHOORZRUOG"
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext))
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext2))

    def test_decrypt(self) -> None:
        """Tests basic string decryption, checking uppercase, lowercase, and white-space."""
        cipher = CaesarCipher(3)
        ciphertext = "KHOORZRUOG"
        ciphertext2 = "khoor zruog"
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext))
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext2))

    def test_encrypt_decrypt(self) -> None:
        """Tests that output of encryption decrypts to its input."""
        cipher = CaesarCipher(7)
        plaintext = "Test input with spaces"
        ciphertext = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(ciphertext)
        self.assertEqual(plaintext.upper().replace(" ", ""), decrypted_plaintext)
