"""
Affine Cipher unit testing suite.
"""

import unittest
from src.affine_cipher import AffineCipher


class TestAffineCipher(unittest.TestCase):
    """This test suite performs testing on all functionality relevant to the AffineCipher class."""

    def test_invalid_a_coefficient(self):
        """degree_one coefficients not invertible modulo 26."""
        self.assertRaises(ValueError, AffineCipher, 3, 0)
        self.assertRaises(ValueError, AffineCipher, 4, 0)
        self.assertRaises(ValueError, AffineCipher, 9, 0)
        self.assertRaises(ValueError, AffineCipher, 25, 0)

        # invertible coefficients shouldn't throw error
        AffineCipher(5, 0)
        AffineCipher(11, 0)
        AffineCipher(19, 0)

    def test_invalid_b_coefficient(self):
        """degree_zero coefficients not in range [0, 26)."""
        self.assertRaises(ValueError, AffineCipher, 1, 26)
        self.assertRaises(ValueError, AffineCipher, 1, 100)
        self.assertRaises(ValueError, AffineCipher, 1, -1)
        self.assertRaises(ValueError, AffineCipher, 1, -100)

        # coefficients within bounds shouldn't throw error
        AffineCipher(1, 0)
        AffineCipher(1, 13)
        AffineCipher(1, 25)

    def test_encrypt(self):
        """Tests basic string encryption, checking uppercase, lowercase, and white-space."""
        cipher = AffineCipher(7, 7)
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_ciphertext = "EJGGBFBWGC"
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext))
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext2))

    def test_decrypt(self):
        """Tests basic string decryption, checking uppercase, lowercase, and white-space."""
        cipher = AffineCipher(7, 7)
        ciphertext = "EJGGBFBWGC"
        ciphertext2 = "ejggb fbwgc"
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext))
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext2))

    def test_encrypt_decrypt(self):
        """Tests that output of encryption decrypts to its input."""
        cipher = AffineCipher(11, 19)
        plaintext = "Test input with spaces"
        ciphertext = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(ciphertext)
        self.assertEqual(plaintext.upper().replace(" ", ""), decrypted_plaintext)
