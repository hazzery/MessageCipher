from src.Caesar_Cipher import CaesarCipher
import unittest


class TestCaesarCipher(unittest.TestCase):

    def test_invalid_coefficient(self):
        with self.assertRaises(ValueError):
            # coefficients not in range [0, 26)
            CaesarCipher(26)
            CaesarCipher(100)
            CaesarCipher(-1)
            CaesarCipher(-100)

    def test_encrypt(self):
        cipher = CaesarCipher(3)
        plaintext = "HELLOWORLD"
        plaintext2 = "hello world"
        expected_ciphertext = "KHOORZRUOG"
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext))
        self.assertEqual(expected_ciphertext, cipher.encrypt(plaintext2))

    def test_decrypt(self):
        cipher = CaesarCipher(3)
        ciphertext = "KHOORZRUOG"
        ciphertext2 = "khoor zruog"
        expected_plaintext = "HELLOWORLD"
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext))
        self.assertEqual(expected_plaintext, cipher.decrypt(ciphertext2))

    def test_encrypt_decrypt(self):
        cipher = CaesarCipher(7)
        plaintext = "HELLO WORLD"
        ciphertext = cipher.encrypt(plaintext)
        decrypted_plaintext = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_plaintext, plaintext.replace(" ", ""))


if __name__ == "__main__":
    unittest.main()
