"""
RSA system unit testing suite.
"""

import unittest
from src.message_cipher.rsa_system import RSA, is_prime, invertible_elements


class TestRSA(unittest.TestCase):
    """This suite tests all functionality relevant to the RSA class."""

    def test_is_prime(self):
        """Prime number input should return `True`."""
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
        """Composite number input should return `False`."""
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
        such that n and x are coprime.
        Expected invertible elements lists were generated using an online calculator.
        """
        expected_invertible_elements = [1, 2, 3, 4]
        self.assertListEqual(
            expected_invertible_elements, sorted(invertible_elements(5))
        )

        expected_invertible_elements = [1, 3, 7, 9]
        self.assertListEqual(
            expected_invertible_elements, sorted(invertible_elements(10))
        )

        expected_invertible_elements = [1, 3, 7, 9, 11, 13, 17, 19]
        self.assertListEqual(
            expected_invertible_elements, sorted(invertible_elements(20))
        )

    def test_init(self):
        """
        Class constructor should correctly calculate product and exponent
        as well as throwing an error for incorrect input.
        """

        prime1 = 5
        prime2 = 7
        rsa = RSA(prime1, prime2)

        # product is the product of prime1 and prime2
        self.assertEqual(prime1 * prime2, rsa.product)

        # exponent must be invertible modulo phi(product)
        # the following line would raise an exception if exponent were not invertible
        pow(rsa.exponent, -1, (prime1 - 1) * (prime2 - 1))

        # prime1 and prime2 must both be prime
        self.assertRaises(ValueError, RSA, 4, 7)
        self.assertRaises(ValueError, RSA, 5, 8)

        # manually specified exponent must be invertible modulo phi(product)
        self.assertRaises(ValueError, RSA, 5, 7, 6)
        self.assertRaises(ValueError, RSA, 5, 7, 8)
        self.assertRaises(ValueError, RSA, 5, 7, 16)

    def test_encrypt(self):
        """Tests basic string encryption, checking uppercase, lowercase, and white-space."""
        cipher = RSA(5, 7, 17)  # manually specified exponent value not random
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_cipher_array = [7, 9, 16, 16, 14, 22, 14, 12, 16, 33]
        self.assertEqual(expected_cipher_array, cipher.encrypt(plaintext))
        self.assertEqual(expected_cipher_array, cipher.encrypt(plaintext2))

    def test_decrypt(self):
        """Tests basic string decryption, checking uppercase, lowercase, and white-space."""
        cipher = RSA(5, 7, 17)  # manually specified exponent value not random
        cipher_array = [7, 9, 16, 16, 14, 22, 14, 12, 16, 33]
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(cipher_array))

    def test_encrypt_decrypt(self):
        """Tests basic string decryption, checking uppercase, lowercase, and white-space."""
        cipher = RSA(5, 7)  # random exponent value
        plaintext = "Test input with spaces"
        cipher_array = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(cipher_array)
        self.assertEqual(plaintext.upper().replace(" ", ""), decrypted_plaintext)

    def test_no_arguments(self):
        """RSA constructed without arguments should generate random primes."""
        cipher = RSA()
        plaintext = "some random string whatever"
        cipher_array = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(cipher_array)
        self.assertEqual(plaintext.upper().replace(" ", ""), decrypted_plaintext)
