import unittest
from py_string_sculptor import string_sculptor


class TestStringSculptor(unittest.TestCase):
    def test_string_cases(self):
        self.assertEqual(string_sculptor("hello"), "hElLo")
        self.assertEqual(string_sculptor("Hello World"), "hElLo wOrLd")
        self.assertEqual(string_sculptor("abc123def"), "aBc123DeF")
        self.assertEqual(string_sculptor("Python3.9!"), "pYtHoN3.9!")
        self.assertEqual(string_sculptor(""), "")
