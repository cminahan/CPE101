# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

#list comprehension tests
import unittest
from list_comp import *
#from objects import *

class TestCases(unittest.TestCase):

   # determines the distance from each point to the origin
   def test_distance_all(self):
      # Add code here.
      list1 = [Point(1,2), Point(0,5), Point(-12,-3), Point(-3, 0)]
      res1 = [2.23606797749979, 5.0, 12.36931687685298, 3.0]
      self.assertEqual(distance_all(list1), res1)
      list2 = [Point(0, -4), Point(9,6), Point(23,0)]
      res1 = [4.0, 10.816653826391969, 23.0]
      self.assertEqual(distance_all(list2), res1)
      list3 = [Point(0,-13), Point(3,8), Point(-9,2)]
      res3 = [13.0, 8.54400374531753, 9.219544457292887]
      self.assertEqual(distance_all(list3), res3)

   # determines if the points are in the first quadrant
   def test_are_in_first_quadrant(self):
      list1 = [Point(1,2), Point(0,5), Point(-12,-3), Point(-3, 0)]
      res1 = [Point(1,2)]
      self.assertEqual(are_in_first_quadrant(list1), res1)
      list2 = [Point(-1,4), Point(4,5), Point(3,6), Point(0,0)]
      res2 = [Point(4,5), Point(3,6)]
      self.assertEqual(are_in_first_quadrant(list2), res2)
      list3 = [Point(-8, 3), Point(2,4), Point(3,18), Point(12,16), Point(-9,8)]
      res3 = [Point(2,4), Point(3,18), Point(12,16)]
      self.assertEqual(are_in_first_quadrant(list3), res3)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

