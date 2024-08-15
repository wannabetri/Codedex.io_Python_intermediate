import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized


class TestStringUtils(unittest.TestCase):
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string(""), "")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("world"), "World")
        self.assertEqual(capitalize_string(""), "")

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Hello"))
        self.assertFalse(is_capitalized("hello"))
        self.assertFalse(is_capitalized(""))

if __name__ == '__main__':
    unittest.main()