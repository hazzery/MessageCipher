"""
This module provides functionality to generate large prime numbers.
All code below is improved upon code sourced from:
https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
"""

import random

NUMBER_OF_BITS = 12


first_primes_list = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
]


def n_bit_random(number_of_bits: int) -> int:
    """Returns a random number between ``2^(number_of_bits - 1) + 1`` and ``2^number_of_bits - 1``

    :param number_of_bits: The desired size (in binary bits) of the random number.
    :return: A random number that is ``number_of_bits`` bits long.
    """
    return random.randrange(2 ** (number_of_bits - 1) + 1, 2**number_of_bits - 1)


def get_low_level_prime(number_of_bits: int) -> int:
    """Generate a prime candidate divisible by first primes.

    :param number_of_bits: The desired size (in binary bits) of the random number.
    :return: A random prime number that is ``number_of_bits`` bits long.
    """
    # Repeat until a number satisfying the test isn't found
    while True:
        # Obtain a random number
        prime_candidate = n_bit_random(number_of_bits)

        for divisor in first_primes_list:
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
            # If no divisor found, return value
            return prime_candidate


def is_miller_rabin_passed(miller_rabin_candidate: int) -> bool:
    """Run 20 iterations of Rabin Miller Primality test.

    :param miller_rabin_candidate: The number to test for primality.
    :return: ``True`` if the number is probably prime, otherwise ``False``
    """

    max_divisions_by_two = 0
    even_component = miller_rabin_candidate - 1

    while even_component % 2 == 0:
        even_component >>= 1
        max_divisions_by_two += 1
    assert 2**max_divisions_by_two * even_component == miller_rabin_candidate - 1

    def trial_composite(round_tester: int) -> bool:
        if pow(round_tester, even_component, miller_rabin_candidate) == 1:
            return False
        for i in range(max_divisions_by_two):
            if (
                pow(round_tester, 2**i * even_component, miller_rabin_candidate)
                == miller_rabin_candidate - 1
            ):
                return False

        return True

    # Set number of trials here
    number_of_rabin_trials = 20
    for _ in range(number_of_rabin_trials):
        round_tester = random.randrange(2, miller_rabin_candidate)
        if trial_composite(round_tester):
            return False

    return True


def generate_large_prime() -> int:
    """Generate a ``NUMBER_OF_BITS``-bit prime number.

    :return: A large prime number.
    """
    prime_candidate = get_low_level_prime(NUMBER_OF_BITS)
    while not is_miller_rabin_passed(prime_candidate):
        prime_candidate = get_low_level_prime(NUMBER_OF_BITS)

    return prime_candidate
