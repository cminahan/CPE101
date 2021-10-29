# LAB 6: Polynomial Function Tests
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from poly import *

class TestPoly(unittest.TestCase):
   #do not delete this part use this to comapre two list
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   #adds the input polynomials
   def test_poly_add2(self):	# Test add function
      self.assertListAlmostEqual(poly_add2([2.3, 4.7, 1.0], [1.2, 2.1, -3.2]), [3.5, 6.8, -2.2])
      self.assertListAlmostEqual(poly_add2([1.4, 3.6, -9.1], [3.2, 4.5, 7.2]), [4.6, 8.1, -1.9])
      self.assertListAlmostEqual(poly_add2([2.4, 0.8, -1.2], [3.2, 7.4, 1.3]), [5.6, 8.2, 0.1])

   #multiplies the input polynomials
   def test_poly_mult2(self):
      self.assertListAlmostEqual(poly_mult2([2.4, 1.5, 3.2], [1.7, 3.2, 0.7]), [4.08, 10.23, 11.92, 11.29, 2.24])
      self.assertListAlmostEqual(poly_mult2([1.4, -5.6, 3.1], [8.1, 3.2, 4.3]), [11.34, -40.88, 13.21, -14.16, 13.33])
      self.assertListAlmostEqual(poly_mult2([6.7, -0.4, 2.7], [3.8, 1.0, 4.6]), [25.46, 5.18, 40.68, 0.86, 12.42])





if __name__ == '__main__':
   unittest.main()
