#at least 3 test cases for each function
import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   #first test for updateAcceleration
   def test_updateAcceleration_1(self):
      self.assertEqual(updateAcceleration(13, 10), 25)
      self.assertEqual(updateAcceleration(7, 15), 20)
      self.assertEqual(updateAcceleration(19, 5), 18)

   def test_updateAltitude(self):
      self.assertEqual(updateAltitude(4, 14, 8), 22)
      self.assertEqual(updateAltitude(12, 7, 5), 21.5)
      self.assertEqual(updateAltitude(13, 17, 4), 32)

   def test_updateVelocity(self):
      self.assertEqual(updateVelocity(12, 13), 25)
      self.assertEqual(updateVelocity(12.1, 9.8), 21.9)
      self.assertEqual(updateVelocity(4.7, 3.5), 8.2)

   def test_updateFuel(self):
      self.assertEqual(updateFuel(12, 8), 4)
      self.assertEqual(updateFuel(24, 7), 17)
      self.assertEqual(updateFuel(4, 1), 3)

 
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

