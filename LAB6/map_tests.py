# Lab 6: Polynomial Functions Test
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from map import*

class TestCases(unittest.TestCase):

    # do not delete this part use this to comapre two list
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    #cubes each value in the input list
    def test_cube_all(self):
        self.assertListAlmostEqual(cube_all([2, 3, 4]), [8, 27, 64])
        self.assertListAlmostEqual(cube_all([1, 5, 6]), [1, 125, 216])
        self.assertListAlmostEqual(cube_all([7, 8, 9]), [343, 512, 729])

    #adds n to each value in the input list
    def test_add_n_to_all(self):
        self.assertListAlmostEqual(add_n_to_all([3, 4, 6], 9), [12, 13, 15])
        self.assertListAlmostEqual(add_n_to_all([2.1, -9.2, 3.7], 1.7), [3.8, -7.5, 5.4])
        self.assertListAlmostEqual(add_n_to_all([4, 8.1, -4.3], 0.3), [4.3, 8.4, -4])

    #checks whether each input value is divisable by 5
    def test_div_by_5_all(self):
        self.assertListAlmostEqual(div_by_5_all([4, 6, 10, 15]), ['False', 'False', 'True', 'True'])
        self.assertListAlmostEqual(div_by_5_all([25, 90, 7, 5]), ['True', 'True', 'False', 'True'])
        self.assertListAlmostEqual(div_by_5_all([14, 3, 30]), ['False', 'False', 'True'])

#Run the unittest
if __name__ == '__main__':
    unittest.main()