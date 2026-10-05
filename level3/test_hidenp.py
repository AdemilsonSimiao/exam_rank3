import unittest
from py_hidenp import hidenp


class TestHidenp(unittest.TestCase):
    def test_true_cases(self):
        self.assertTrue(hidenp("abc", "a1b2c3"))
        self.assertTrue(hidenp("ace", "abcde"))
        self.assertTrue(hidenp("", "abc"))
        self.assertTrue(hidenp("sing","subsequence testing"))

    def test_false_cases(self):
        self.assertFalse(hidenp("aec", "abcde"))
        self.assertFalse(hidenp("abc", "ab"))
        self.assertFalse(hidenp("aaaa", "aaa"))