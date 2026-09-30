import unittest
from py_cryptic_sorter import cryptic_sorter

class TestCrypticSorter(unittest.TestCase):
    def test_case_insensitively(self):
       input = ["apple","cat","banana","dog","elephant"]
       output = ["cat","dog","apple","banana","elephant"]
       self.assertEqual(cryptic_sorter(input), output)
    
    def test_case_lexically(self):
        input = ["aaa","bbb","AAA","BBB"]
        output = ["aaa", "AAA", "bbb", "BBB"]
        self.assertEqual(cryptic_sorter(input), output)
    
    def test_case_order(self):
        input = ["hello","world","hi","test"]
        output = ["hi","test","hello","world"]
        self.assertEqual(cryptic_sorter(input), output)

    def test_case_edge(self):
        self.assertEqual(cryptic_sorter([]), [])
        self.assertEqual(cryptic_sorter([""]), [""])
        self.assertEqual(cryptic_sorter(["AAA", "aaa"]), ["AAA", "aaa"])


if __name__ == "__main__":
    unittest.main()