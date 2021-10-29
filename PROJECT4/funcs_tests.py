# Project 4 - Calcudoku
# Section: CPE101 - 03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from funcs import*

class TestCases(unittest.TestCase):
    # do not delete this part use this to comapre two list
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    # return true if all rows contain no duplicate number
    def test_validate_rows(self):
        self.assertTrue(validate_rows([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]))
        self.assertTrue(validate_rows([[1,0,2,3,4],[1,3,4,6,0],[0,0,0,0,0],[1,0,3,5,4],[1,2,3,4,5]]))
        self.assertFalse(validate_rows([[1,1,1,1,1],[1,2,2,3,4],[1,2,3,4,5],[0,0,0,0,0],[1,2,3,4,4]]))

    # return true if all columns contain no duplicate numbers
    def test_validate_columns(self):
        self.assertTrue(validate_columns([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]))
        self.assertFalse(validate_columns([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,4],[2,2,3,4,3],[1,1,1,1,1]]))
        self.assertFalse(validate_columns([[1,0,0,0,0],[1,1,1,1,1],[1,2,3,4,5],[0,3,4,2,3],[3,4,5,3,4]]))

    # return true if the cages are correct
    def test_validate_cages(self):
        grid1 = [[4, 1, 2, 5, 3], [1, 5, 4, 3, 2], [2, 3, 5, 4, 1], [3, 4, 1, 2, 5], [5, 2, 3, 1, 4]]
        cage1 = [[5, 0, 5], [8, 1, 2, 6], [8, 3, 8], [6, 4, 9, 14], [13, 7, 12, 13], [5, 10, 15], [14, 11, 16, 20, 21],
                 [6, 17, 18, 22], [10, 19, 23, 24]]
        self.assertTrue(validate_cages(grid1,cage1))
        grid2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        cage2 = [[34,3,4],[4,5,6],[2,4,5,4],[1,3,5,]]
        self.assertTrue(validate_cages(grid2,cage2))
        grid3 = [[1,2,3,4,4],[1,2,3,4,3],[1,1,1,1,1],[2,2,2,2,2],[2,3,4,5,2]]
        cage3 = [[3,4,5],[8,17,23],[12,4,21]]
        self.assertFalse(validate_cages(grid3,cage3))

    #returns true if all function return true
    def test_validate_all(self):
        grid1 = [[4, 1, 2, 5, 3], [1, 5, 4, 3, 2], [2, 3, 5, 4, 1], [3, 4, 1, 2, 5], [5, 2, 3, 1, 4]]
        cage1 = [[5, 0, 5], [8, 1, 2, 6], [8, 3, 8], [6, 4, 9, 14], [13, 7, 12, 13], [5, 10, 15], [14, 11, 16, 20, 21],
                 [6, 17, 18, 22], [10, 19, 23, 24]]
        self.assertTrue(validate_all(grid1,cage1))
        grid2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        cage2 = [[34,3,4],[4,5,6],[2,4,5,4],[1,3,5,]]
        self.assertTrue(validate_all(grid2,cage2))
        grid3 = [[1,2,3,4,4],[1,2,3,4,3],[1,1,1,1,1],[2,2,2,2,2],[2,3,4,5,2]]
        cage3 = [[3,4,5],[8,17,23],[12,4,21]]
        self.assertFalse(validate_all(grid3,cage3))


if __name__ == '__main__':
    unittest.main()