import unittest
from py_string_permutation_checker import string_permutation_checker


class TestStringPermutationChecker(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(string_permutation_checker("abc", "bca"))
        self.assertTrue(string_permutation_checker("listen", "silent"))
        self.assertTrue(string_permutation_checker("", ""))
        self.assertTrue(string_permutation_checker("a gentleman","elegant man"))

    def test_false_cases(self):
        self.assertFalse(string_permutation_checker("abc", "def"))
        self.assertFalse(string_permutation_checker("hello", "bello"))
        self.assertFalse(string_permutation_checker("a", ""))
        self.assertFalse(string_permutation_checker("Abc", "abc"))
