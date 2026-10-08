import unittest
from py_twist_sequence import twist_sequence

class TestTwistSequence(unittest.TestCase):
    def test_sequence_cases(self):
        self.assertEqual(twist_sequence([1,2,3,4,5], 2), [4,5,1,2,3])
        self.assertEqual(twist_sequence([1,2,3], 1), [3,1,2])
        self.assertEqual(twist_sequence([1,2,3,4], 0), [1,2,3,4])
        self.assertEqual(twist_sequence([1,2,3], 5), [2,3,1])
        self.assertEqual(twist_sequence([], 3), [])
