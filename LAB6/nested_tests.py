# Lab 6: Polynomial Functions Test
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from nested import*

class TestCase(unittest.TestCase):

    # do not delete this part use this to comapre two list
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    # takes a nested list returns a list of integers such that each integer is a product of its inner list
    def test_product(self):
        self.assertAlmostEqual(product([[1, 2], [2, 3, 4], [-2, 5]]), [2, 24, -10])
        self.assertAlmostEqual(product([[3, 4], [0, 4, 1], [3, 9]]), [12, 0, 27])
        self.assertAlmostEqual(product([[5, 3, 2], [4, 1, 5], [6, 3]]), [30, 20, 18])


if __name__ == '__main__':
    unittest.main()