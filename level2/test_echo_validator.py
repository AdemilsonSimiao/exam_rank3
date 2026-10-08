import unittest
from py_echo_validator import echo_validator


class TestMirrorMatrix(unittest.TestCase):
    def test_true_case(self):
        self.assertTrue(echo_validator("racecar"))
        self.assertTrue(echo_validator("A man a plan a canal Panama"))
        self.assertTrue(echo_validator("Was it a car or a cat I saw"))
        self.assertTrue(echo_validator("Madam Im Adam"))
        self.assertTrue(echo_validator("a"))
    
    def test_false_case(self):
        self.assertFalse(echo_validator("race a car"))
        self.assertFalse(echo_validator("hello"))
        self.assertFalse(echo_validator(""))
        self.assertFalse(echo_validator("123"))


if __name__ == "__main__":
    unittest.main()
