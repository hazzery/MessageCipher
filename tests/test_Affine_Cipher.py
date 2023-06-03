from src.Affine_Cipher import AffineCipher
import unittest


class TestAffineCipher(unittest.TestCase):

    def test_invalid_a_coefficient(self):
        with self.assertRaises(ValueError):
            # a coefficients not invertible modulo 26
            AffineCipher(3, 0)
            AffineCipher(4, 0)
            AffineCipher(9, 0)
            AffineCipher(25, 0)

    def test_invalid_b_coefficient(self):
        with self.assertRaises(ValueError):
            # b coefficients not in range [0, 26)
            AffineCipher(1, 26)
            AffineCipher(1, 100)
            AffineCipher(1, -1)
            AffineCipher(1, -100)

    def test_encrypt(self):
        cipher = AffineCipher(7, 7)
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_ciphertext = "EJGGBFBWGC"
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext))
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext2))

    def test_decrypt(self):
        cipher = AffineCipher(7, 7)
        ciphertext = "EJGGBFBWGC"
        ciphertext2 = "ejggb fbwgc"
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext))
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext2))


if __name__ == '__main__':
    unittest.main()
