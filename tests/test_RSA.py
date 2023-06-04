"""
RSA system unit testing suite.
"""
from src.RSA_System import RSA, is_prime, invertible_elements
import unittest


class TestRSA(unittest.TestCase):
    """This suite tests all functionality relevant to the RSA class"""

    def test_is_prime(self):
        """Prime number input should return `True`"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))

    def test_isnt_prime(self):
        """Composite number input should return `False`"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))

    def test_invertible_elements(self):
        """
        An invertible element modulo n 'x' is an integer in range [1, n)
        such that n and x are coprime
        """

        expected_invertible_elements = [1, 2, 3, 4]
        self.assertListEqual(sorted(invertible_elements(5)), expected_invertible_elements)

        expected_invertible_elements = [1, 3, 7, 9]
        self.assertListEqual(sorted(invertible_elements(10)), expected_invertible_elements)

        expected_invertible_elements = [1, 3, 7, 9, 11, 13, 17, 19]
        self.assertListEqual(sorted(invertible_elements(20)), expected_invertible_elements)

    def test_init(self):
        """
        Class constructor should correctly calculate product and exponent
        As well as throwing an error upon incorrect input
        """

        p = 5
        q = 7
        rsa = RSA(p, q)

        # n is the product of p and q
        self.assertEqual(rsa.n, p * q)

        # e must be invertible modulo phi(n)
        # this would raise an exception if it were not true
        pow(rsa.e, -1, (p - 1) * (q - 1))

        # p and q must both be prime
        self.assertRaises(ValueError, RSA, 4, 7)
        self.assertRaises(ValueError, RSA, 5, 8)

        # manually specified e must be invertible modulo phi(n)
        self.assertRaises(ValueError, RSA, 5, 7, 6)
        self.assertRaises(ValueError, RSA, 5, 7, 8)
        self.assertRaises(ValueError, RSA, 5, 7, 16)

    def test_encrypt(self):
        """Tests basic string encryption, checking uppercase, lowercase, and white-space"""
        cipher = RSA(5, 7, 17)  # manually specified e value not random
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_cipher_array = [7, 9, 16, 16, 14, 22, 14, 12, 16, 33]
        self.assertEqual(expected_cipher_array, cipher.encrypt(plaintext))
        self.assertEqual(expected_cipher_array, cipher.encrypt(plaintext2))

    def test_decrypt(self):
        """Tests basic string decryption, checking uppercase, lowercase, and white-space"""
        cipher = RSA(5, 7, 17)  # manually specified e value not random
        cipher_array = [7, 9, 16, 16, 14, 22, 14, 12, 16, 33]
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(cipher_array))

    def test_encrypt_decrypt(self):
        """Tests basic string decryption, checking uppercase, lowercase, and white-space"""
        cipher = RSA(5, 7)  # random e value
        plaintext = "Test input with spaces"
        cipher_array = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(cipher_array)
        self.assertEqual(decrypted_plaintext, plaintext.upper().replace(" ", ""))
