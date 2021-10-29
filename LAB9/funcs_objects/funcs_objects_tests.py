# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

#unittest for objects
import unittest
from objects import *
from funcs_objects import*

class TestCases(unittest.TestCase):
   # test the Point class
   def test_point(self):
      point1 = Point(1, 2)
      point2 = Point(-3, 2)
      point3 = point1
      point4 = Point(12, -9)
      self.assertTrue(point1 == point3)
      self.assertFalse(point2 == point4)
      self.assertFalse(point3 == point4)

   # test the Circle class
   def test_circle(self):
      # Add code here.
      circle1 = Circle(Point(1,2), 4)
      circle2 = circle1
      circle3 = Circle(Point(3,-4), 6)
      circle4 = Circle(Point(12, -9), 2)
      self.assertTrue(circle1 == circle2)
      self.assertFalse(circle3 == circle4)
      self.assertFalse(circle3 == circle2)

   # determines distance between two points
   def test_distance(self):
      point1 = Point(0,0)
      point2 = Point(0,5)
      point3 = Point(12,5)
      point4 = Point(-3,-5)
      self.assertEqual(distance(point1, point2), 5.00)
      self.assertEqual(distance(point2, point3), 12.00)
      self.assertEqual(distance(point3, point4), 18.027756377319946)

   # determines if two circles overlap
   def test_circle_overlap(self):
      circle1 = Circle(Point(0,0), 4)
      circle2 = Circle(Point(0,5), 2)
      circle3 = Circle(Point(12,5), 5)
      circle4 = Circle(Point(-3,-5), 15)
      self.assertTrue(circle_overlap(circle1, circle2))
      self.assertFalse(circle_overlap(circle2, circle3))
      self.assertTrue(circle_overlap(circle3, circle4))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

