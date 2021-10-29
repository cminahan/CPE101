# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

#object equality unitest
import unittest
#from objects import *
from utility import*

class TestCases(unittest.TestCase):
   def test_equality(self):
      point1 = Point(1, 2)
      point2 = Point(-3, 2)
      point3 = point1
      point4 = Point(-3, 2)
      point5 = point4
      self.assertEqual(point1, point3)
      self.assertEqual(point2, point4)
      self.assertFalse(point3 == point4)
      self.assertEqual(point4, point5)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

