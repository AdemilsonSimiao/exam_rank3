import unittest
from py_pattern_tracker import pattern_tracker


class TestPatternTracker(unittest.TestCase):
    def test_digit_alpha(self):
        self.assertEqual(pattern_tracker("12a34"), 2)
        self.assertEqual(pattern_tracker("1a2b3c4"), 0)
        self.assertEqual(pattern_tracker("12a34"), 2)
    
    def test_only_digit(self):
        self.assertEqual(pattern_tracker("123"), 2)
        self.assertEqual(pattern_tracker("987654321"), 0)
        self.assertEqual(pattern_tracker("01234567"), 7)
        self.assertEqual(pattern_tracker("112233"), 2)
    
    def test_only_alpha(self):
        self.assertEqual(pattern_tracker("abc"), 0)
