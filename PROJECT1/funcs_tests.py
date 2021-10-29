# Project 1 
# 
# Name: Your Name
# Instructor: S. Einakian 
# Section: Your Section

import unittest
from projFuncs import *

class TestCases(unittest.TestCase):

   def test_convetPoundsToKG(self):
      self.assertAlmostEqual(convertPoundsToKG(100), 45.3592)
      self.assertAlmostEqual(convertPoundsToKG(148), 67.131616)

   def test_getMassOfObject(self):
      self.assertEqual(getMassOfObject('t'), 0.1)
      self.assertEqual(getMassOfObject('p'), 1.0)
      self.assertEqual(getMassOfObject('r'), 3.0)
      self.assertEqual(getMassOfObject('g'), 5.3)
      self.assertEqual(getMassOfObject('l'), 9.07)
      self.assertEqual(getMassOfObject('x'), 0.0)

   def test_getVelocityOfObject(self):
      self.assertEqual(getVelocityOfObject(10), 7)
      self.assertAlmostEqual(getVelocityOfObject(27), 11.50217371)

   def test_getVelocityOfSkater(self):
      self.assertAlmostEqual(getVelocityOfSkater(49, 3, 17), 1.040816327)
      self.assertAlmostEqual(getVelocityOfSkater(54, 7, 32), 4.148148148)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

