import unittest
from py_shadow_merge import shadow_merge


class TestShadowMerge(unittest.TestCase):
    def test_merge_cases(self):
        self.assertEqual(shadow_merge([1,3,5], [2,4,6]), [1,2,3,4,5,6])
        self.assertEqual(shadow_merge([1,2,3], [4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(shadow_merge([1], [2,3,4]), [1,2,3,4])
        self.assertEqual(shadow_merge([], [1,2,3]), [1,2,3])
        self.assertEqual(shadow_merge([1,1,2], [1,3,3]), [1,1,1,2,3,3])
