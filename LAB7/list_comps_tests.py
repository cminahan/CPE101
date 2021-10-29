# Lab 7
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from list_comps import*

class TestCases(unittest.TestCase):
    # do not delete this part use this to comapre two list
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    #Map Patterns

    #returns a list with the square of each value in the list
    def test_square_all(self):
        self.assertListAlmostEqual(square_all([1, 2, 3]), [1, 4, 9])
        self.assertListAlmostEqual(square_all([4, 7, 5]), [16, 49, 25])
        self.assertListAlmostEqual(square_all([0, 9, 8, 6]), [0, 81, 64, 36])

    #returns a list of 1 and 0 depending on whether the value is even or odd
    def test_is_even_all(self):
        self.assertListAlmostEqual(is_even_all([2, 3, 4, 5]), [1, 0, 1, 0])
        self.assertListAlmostEqual(is_even_all([3, 15, 48]), [0, 0, 1])
        self.assertListAlmostEqual(is_even_all([12, 14, 16]), [1, 1, 1])

    #returns a list with n multiplied with each element in the given list
    def test_mult_with_n(self):
        self.assertListAlmostEqual(mult_with_n([1, 2, 3], 5), [5, 10, 15])
        self.assertListAlmostEqual(mult_with_n([2, 4, 3], 4), [8, 16, 12])
        self.assertListAlmostEqual(mult_with_n([7, 3, 0, 9], 3), [21, 9, 0, 27])

    #Filter Patterns

    #returns a list of all negatives value in given list
    def test_negative_list(self):
        self.assertListAlmostEqual(negative_list([-1, 3, -4, 5, -18]), [-1, -4, -18])
        self.assertListAlmostEqual(negative_list([2, -4, 9, 7]), [-4])
        self.assertListAlmostEqual(negative_list([-1, -2, -90]), [-1, -2, -90])

    #returns a list of value in the given list that are smaller than n
    def test_smaller_than_n(self):
        self.assertListAlmostEqual(smaller_than_n([9, 3, 4, 5, 6], 5), [3, 4])
        self.assertListAlmostEqual(smaller_than_n([3, -1, 5, -2], 0), [-1, -2])
        self.assertListAlmostEqual(smaller_than_n([90, 67, 35, 50], 100), [90, 67, 35, 50])

    #returns a list of value in the given list that are between the given intervals (exclusive)
    def test_between_range(self):
        self.assertListAlmostEqual(between_range([2, 4, 5, 14, 7], 4, 10), [5, 7])
        self.assertListAlmostEqual(between_range([1, -4, 6, 7.5], 2, 8), [6, 7.5])
        self.assertListAlmostEqual(between_range([-.4, -9.8, 3.2, 7.3], -.5, 7.3), [-.4, 3.2])

if __name__ == '__main__':
    unittest.main()