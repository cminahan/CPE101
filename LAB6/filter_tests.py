# Lab 6: Polynomial Functions Test
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from filter import*

class TestCases(unittest.TestCase):

    # do not delete this part use this to comapre two list
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    #returns a list of all even values in the input list
    def test_are_even(self):
        self.assertAlmostEqual(are_even([3, 5, 2, 6, 8]), [2, 6, 8])
        self.assertAlmostEqual(are_even([18, 3, 7, 26]), [18, 26])
        self.assertAlmostEqual(are_even([4, 6, 7, 90]), [4, 6, 90])

    #returns a a list with no duplicates
    def test_remove_duplicates(self):
        self.assertAlmostEqual(remove_duplicates([3, 4, 2, 5, 2, 1]), [3, 4, 2, 5, 1])
        self.assertAlmostEqual(remove_duplicates([1, 1, 1, 1, 4, 2, 1]), [1, 4, 2])
        self.assertAlmostEqual(remove_duplicates([2.3, 4.2, 3.5, 4.2, 7]), [2.3, 4.2, 3.5, 7])

    #returns list of all input values divisable by n
    def test_divisable_by_n(self):
        self.assertAlmostEqual(are_divisable_by_n([3, 7, 9, 12], 3), [3, 9, 12])
        self.assertAlmostEqual(are_divisable_by_n([7, 30, 49, 20, 1], 7), [7, 49])
        self.assertAlmostEqual(are_divisable_by_n([12, 16, 7, 23], 4), [12, 16])




if __name__ == '__main__':
    unittest.main()