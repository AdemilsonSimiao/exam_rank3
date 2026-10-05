import unittest
from py_number_base_converter import number_base_converter


class TestNumberBaseConverter(unittest.TestCase):
    def test_decimal(self):
        self.assertEqual(number_base_converter("1010", 2, 10), "10")
        self.assertEqual(number_base_converter("Z", 36, 10), "35")

    def test_bases_decimal(self):
        self.assertEqual(number_base_converter("FF", 16, 10), "255")

    def test_invert_bases(self):
        self.assertEqual(number_base_converter("255", 10, 16), "FF")
        self.assertEqual(number_base_converter("35", 10, 36), "Z")
    
    def test_binary_base(self):
        self.assertEqual(number_base_converter("123", 10, 2), "1111011")
    
    def test_ERROR(self):
        self.assertEqual(number_base_converter("123", 1, 10), "ERROR")
        self.assertEqual(number_base_converter("G", 16, 10), "ERROR")
