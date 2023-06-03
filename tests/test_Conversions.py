from src.Conversions import int_to_char, char_to_int
import unittest


class TestConversions(unittest.TestCase):

    def test_int_to_char(self):
        self.assertEqual('a', int_to_char(0))
        self.assertEqual('f', int_to_char(5))
        self.assertEqual('z', int_to_char(25))

    def test_char_to_int(self):
        self.assertEqual(0, char_to_int('a'))
        self.assertEqual(5, char_to_int('f'))
        self.assertEqual(25, char_to_int('z'))

    def test_invalid_number(self):
        self.assertRaises(ValueError, int_to_char, -1)
        self.assertRaises(ValueError, int_to_char, 26)
        self.assertRaises(ValueError, int_to_char, 100)

    def test_invalid_char(self):
        self.assertRaises(ValueError, char_to_int, '@')
        self.assertRaises(ValueError, char_to_int, '.')
        self.assertRaises(TypeError, char_to_int, "ab")
        self.assertRaises(TypeError, char_to_int, "Hello World")
