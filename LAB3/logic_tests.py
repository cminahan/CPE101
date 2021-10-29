# Lab 3
#
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101 03

import unittest
from logic import*

#You can delete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_is_odd (self):
      self.assertTrue(is_odd(3))
      self.assertFalse(is_odd(4))
      self.assertFalse(is_odd(-78))

   def test_in_an_interval(self):
      self.assertFalse(in_an_interval(-10))
      self.assertTrue(in_an_interval(1))
      self.assertTrue(in_an_interval(9))
      self.assertTrue(in_an_interval(20))
      self.assertFalse(in_an_interval(52))
      self.assertTrue(in_an_interval(137))

   def test_is_divisible_in_interval(self):
      self.assertTrue(is_divisible_in_interval(150, 30))
      self.assertFalse(is_divisible_in_interval(10, 2))
      self.assertFalse(is_divisible_in_interval(30.9, 15.09))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

