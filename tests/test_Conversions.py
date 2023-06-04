"""
int-char conversion unit testing suite.
"""

from src.Conversions import int_to_char, char_to_int
import unittest


class TestConversions(unittest.TestCase):
    """
    This suite tests the functionality of:
        the int to char conversion function and
        the char to int conversion function
    """

    def test_int_to_char(self):
        """int -> char: Basic expected input"""
        self.assertEqual('a', int_to_char(0))
        self.assertEqual('f', int_to_char(5))
        self.assertEqual('z', int_to_char(25))

    def test_char_to_int(self):
        """char -> int: Basic expected input"""
        self.assertEqual(0, char_to_int('a'))
        self.assertEqual(5, char_to_int('f'))
        self.assertEqual(25, char_to_int('z'))

    def test_invalid_number(self):
        """int -> char: incorrect input"""
        self.assertRaises(ValueError, int_to_char, -1)
        self.assertRaises(ValueError, int_to_char, 26)
        self.assertRaises(ValueError, int_to_char, 100)

    def test_invalid_char(self):
        """char -> int: incorrect input"""
        self.assertRaises(ValueError, char_to_int, '@')
        self.assertRaises(ValueError, char_to_int, '.')
        self.assertRaises(TypeError, char_to_int, "ab")
        self.assertRaises(TypeError, char_to_int, "Hello World")
