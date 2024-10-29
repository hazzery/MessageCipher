"""Integer to character conversion unit testing suite."""

import unittest

from src.message_cipher.conversions import char_to_int, int_to_char


class TestConversions(unittest.TestCase):
    """Verify conversion functionality."""

    def test_int_to_char(self) -> None:
        """Check int -> char: Basic expected input."""
        self.assertEqual("a", int_to_char(0))
        self.assertEqual("f", int_to_char(5))
        self.assertEqual("z", int_to_char(25))

    def test_char_to_int(self) -> None:
        """Check char -> int: Basic expected input."""
        self.assertEqual(0, char_to_int("a"))
        self.assertEqual(5, char_to_int("f"))
        self.assertEqual(25, char_to_int("z"))

    def test_invalid_number(self) -> None:
        """Check int -> char: incorrect input."""
        self.assertRaises(ValueError, int_to_char, -1)
        self.assertRaises(ValueError, int_to_char, 26)
        self.assertRaises(ValueError, int_to_char, 100)

    def test_invalid_char(self) -> None:
        """Check char -> int: incorrect input."""
        self.assertRaises(ValueError, char_to_int, "@")
        self.assertRaises(ValueError, char_to_int, ".")
        self.assertRaises(TypeError, char_to_int, "ab")
        self.assertRaises(TypeError, char_to_int, "Hello World")
