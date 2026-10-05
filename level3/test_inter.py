import unittest
from py_inter import inter


class TestInter(unittest.TestCase):
    def test_inter(self):
        self.assertEqual(inter("hello", "world"), "lo")
        self.assertEqual(inter("banana", "band"), "ban")
        self.assertEqual(inter("abcabc", "bc"), "bc")
    
    def test_empty(self):
        self.assertEqual(inter("abc", "xyz"), "")
        self.assertEqual(inter("", "abc"), "")
