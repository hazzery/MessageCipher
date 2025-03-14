"""Affine Cipher unit testing suite."""

import unittest

from src.message_cipher.affine_cipher import AffineCipher


class TestAffineCipher(unittest.TestCase):
    """Rest suite to perform testing on all functionality relevant to the AffineCipher class."""

    def test_valid_coefficients_no_error_thrown(self) -> None:
        """Assert no exceptions.

        The AffineCipher class should be constructable
        if both coefficients are invertible modulo 26.
        """
        AffineCipher(5, 0)
        AffineCipher(11, 0)
        AffineCipher(19, 0)

    def test_invalid_a_coefficient_throws_value_error(self) -> None:
        """degree_one coefficients not invertible modulo 26."""
        self.assertRaises(ValueError, AffineCipher, 2, 0)
        self.assertRaises(ValueError, AffineCipher, 6, 0)
        self.assertRaises(ValueError, AffineCipher, 13, 0)
        self.assertRaises(ValueError, AffineCipher, 26, 0)

    def test_invalid_b_coefficient(self) -> None:
        """degree_zero coefficients not in range [0, 26)."""
        self.assertRaises(ValueError, AffineCipher, 1, 26)
        self.assertRaises(ValueError, AffineCipher, 1, 100)
        self.assertRaises(ValueError, AffineCipher, 1, -1)
        self.assertRaises(ValueError, AffineCipher, 1, -100)

        # coefficients within bounds shouldn't throw error
        AffineCipher(1, 0)
        AffineCipher(1, 13)
        AffineCipher(1, 25)

    def test_encrypt(self) -> None:
        """Tests basic string encryption, checking uppercase, lowercase, and white-space."""
        cipher = AffineCipher(7, 11)
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_ciphertext = "INKKFJFAKG"
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext))
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext2))

    def test_decrypt(self) -> None:
        """Tests basic string decryption, checking uppercase, lowercase, and white-space."""
        cipher = AffineCipher(11, 13)
        ciphertext = "MFEELVLSEU"
        ciphertext2 = "mfeel vlseu"
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext))
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext2))

    def test_encrypt_decrypt(self) -> None:
        """Tests that output of encryption decrypts to its input."""
        cipher = AffineCipher(25, 17)
        plaintext = "Test input with spaces"
        ciphertext = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(ciphertext)
        self.assertEqual(plaintext.upper().replace(" ", ""), decrypted_plaintext)
