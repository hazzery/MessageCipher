"""
Prime generator unit testing suite.
"""

from time import perf_counter
import unittest

from src.message_cipher.prime_generator import (
    n_bit_random,
    get_low_level_prime,
    is_miller_rabin_passed,
    generate_large_prime,
    NUMBER_OF_BITS,
)


class TestPrimeGenerator(unittest.TestCase):
    """
    This suite tests all functionality relevant to the prime generator module.
    """

    def test_n_bit_random_size(self) -> None:
        """
        Test that the n-bit random number generator
        returns a number of the correct size.
        """
        # self.assertEqual(2, len(bin(n_bit_random(2))))
        self.assertEqual(4, len(bin(n_bit_random(4))) - 2)
        self.assertEqual(8, len(bin(n_bit_random(8))) - 2)
        self.assertEqual(16, len(bin(n_bit_random(16))) - 2)
        self.assertEqual(32, len(bin(n_bit_random(32))) - 2)
        self.assertEqual(64, len(bin(n_bit_random(64))) - 2)
        self.assertEqual(128, len(bin(n_bit_random(128))) - 2)
        self.assertEqual(256, len(bin(n_bit_random(256))) - 2)

    def test_get_low_level_prime_speed(self) -> None:
        """
        Test that the low-level prime generator is fast enough.
        """
        start_time = perf_counter()
        get_low_level_prime(NUMBER_OF_BITS)
        end_time = perf_counter()
        self.assertLess(end_time - start_time, 0.005)

    def test_is_miller_rabin_passed_speed(self) -> None:
        """
        Test that the Miller-Rabin primality test is fast enough.
        """
        start_time = perf_counter()
        candidate = get_low_level_prime(NUMBER_OF_BITS)
        is_miller_rabin_passed(candidate)
        end_time = perf_counter()
        self.assertLess(end_time - start_time, 0.01)

    def test_generate_large_prime_speed(self) -> None:
        """
        Test that the large prime generator is fast enough.
        """
        start_time = perf_counter()
        generate_large_prime()
        end_time = perf_counter()
        self.assertLess(end_time - start_time, 0.1)
