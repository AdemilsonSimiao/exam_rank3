import unittest
from py_bracket_validator import bracket_validator

class TestBracketValidator(unittest.TestCase):
    def test_true_validates(self):
        self.assertTrue(bracket_validator("()"))
        self.assertTrue(bracket_validator("[]"))
        self.assertTrue(bracket_validator("{}"))
        self.assertTrue(bracket_validator("([{}])"))
        self.assertTrue(bracket_validator("([])"))
        self.assertTrue(bracket_validator("hello(world)"))
        self.assertTrue(bracket_validator(""))
    
    def test_false_validates(self):
        self.assertFalse(bracket_validator("([)]"))
        self.assertFalse(bracket_validator("("))
        self.assertFalse(bracket_validator("]"))
        self.assertFalse(bracket_validator("{"))
        self.assertFalse(bracket_validator("}"))
        self.assertFalse(bracket_validator("({)}"))
        self.assertFalse(bracket_validator("((())"))


if __name__ == "__main__":
    unittest.main()