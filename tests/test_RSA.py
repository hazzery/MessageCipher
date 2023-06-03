from src.RSA_System import RSA, is_prime, invertible_elements
import unittest


class TestRSA(unittest.TestCase):
    def test_is_prime(self):
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
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))

    def test_init(self):
        p = 5
        q = 7
        rsa = RSA(p, q)
        self.assertEqual(rsa.n, p * q)
        self.assertEqual(1, (p - 1) * (q - 1))

    def test_init_nonprime(self):
        with self.assertRaises(ValueError):
            RSA(4, 7)

    def test_invertible_elements(self):
        # self.assertEqual(invertible_elements(), expected_invertible_elements)
        pass


if __name__ == '__main__':
    unittest.main()
