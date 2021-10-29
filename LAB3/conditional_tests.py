# Lab 3
#
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101 03

import unittest
from conditional import*

#You can delete pass after wrinting your code
class TestCases(unittest.TestCase):
   def test_max_of_2(self):
      # Add code here.
      self.assertEqual(max_of_2(1,2), 2)
      self.assertEqual(max_of_2(3, -9), 3)
      self.assertEqual(max_of_2(34.89, 78.8393), 78.8393)


   def test_max_of_3(self):
      self.assertEqual(max_of_3(1.89, 2, 3), 3)
      self.assertEqual(max_of_3(8, 6.7, 7), 8)
      self.assertEqual(max_of_3(49.92374, 56.903, 34.12345), 56.903)


   def test_rental_late_fee(self):
      self.assertEqual(rental_late_fee(-2), 0)
      self.assertEqual(rental_late_fee(7), 20)
      self.assertEqual(rental_late_fee(3), 15)
      self.assertEqual(rental_late_fee(14), 29)
      self.assertEqual(rental_late_fee(76), 100)
      self.assertEqual(rental_late_fee(0), 0)
      self.assertEqual(rental_late_fee(5), 15)
      self.assertEqual(rental_late_fee(12), 20)
      self.assertEqual(rental_late_fee(22), 29)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

