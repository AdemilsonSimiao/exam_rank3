import unittest
from py_mirror_matrix import mirror_matrix

class TestMirrorMatrix(unittest.TestCase):
    def test_tuple_mirror(self):
        inputting = [[1,2,3],[4,5,6]]
        output = [[3,2,1],[6,5,4]]
        self.assertEqual(mirror_matrix(inputting), output)

    def test_list_mirror(self):
        inputting = [[1,2],[3,4],[5,6]]
        output = [[2,1],[4,3],[6,5]]
        self.assertEqual(mirror_matrix(inputting), output)

    def test_no_mirror(self):
        inputting = [[7]]
        output = [[7]]
        self.assertEqual(mirror_matrix(inputting), output)
    
    def test_basic_mirror(self):
        inputting = [[1,2,3,4]]
        output = [[4,3,2,1]]
        self.assertEqual(mirror_matrix(inputting), output)
    
    def test_negative_mirror(self):
        inputting = [[-1,-2],[-3,-4]]
        output = [[-2,-1],[-4,-3]]
        self.assertEqual(mirror_matrix(inputting), output)


if __name__ == "__main__":
    unittest.main()
