# Lab 2 Test Cases
# Name: Claire Minahan
# Section: CPE101 03
##############################################################
import unittest
from funcs import *


class TestCases(unittest.TestCase):
    def test_do_math(self):
        # Add code here.
        self.assertEqual(do_math(0, 0), 0.0)
        self.assertEqual(do_math(1, 2), 25/12)

    def test_quadratic_formula1(self):
        # Add code here.
        self.assertEqual(quadratic_formula1(1,-1,-6), 3.0)
        self.assertEqual(quadratic_formula1(2,-5,-12), 4.0)

    def test_quadratic_formula2(self):
        # Add code here.
        self.assertEqual(quadratic_formula2(1,-1,-6), -2.0)
        self.assertEqual(quadratic_formula2(2,-5,-12), -1.5)

    def test_distance(self):
        # Add code here.
        self.assertEqual(distance(4,3,0,0), 5.0)
        self.assertEqual(distance(8,9,1,9), 7.0)

    def test_is_negative(self):
        # Add code here.
        self.assertTrue(is_negative(-9))
        self.assertFalse(is_negative(45))

    def test_dividable_by_7(self):
        # Add code here.
        self.assertTrue(dividable_by_7(49))
        self.assertFalse(dividable_by_7(90))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
