import unittest
from py_anagram import anagram


class TestAnagram(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(anagram("listen", "silent"))
        self.assertTrue(anagram("Triangle", "Integral"))
        self.assertTrue(anagram("Dormitory", "Dirty Room"))
        self.assertTrue(anagram("", ""))
    
    def test_false_cases(self):
        self.assertFalse(anagram("hello", "world"))
        self.assertFalse(anagram("abc", "abcc"))
