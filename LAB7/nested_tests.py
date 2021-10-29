# Lab 7
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

import unittest
from nested import*

class TestCases(unittest.TestCase):
    # do not delete this part use this to comapre two list
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    #group elements form list into groups of three
    def test_groups_of_3(self):
        self.assertListAlmostEqual(groups_of_3([1,2,3,4,5,6,7,8,9]), [[1,2,3], [4,5,6], [7,8,9]])
        self.assertListAlmostEqual(groups_of_3([1,2,3,4,5]), [[1,2,3], [4,5]])
        self.assertListAlmostEqual(groups_of_3([4,5,6,7,8,9,0]), [[4,5,6], [7,8,9], [0]])

    #return a list that contains only the final element of each innner list
    def test_final_value(self):
        self.assertListAlmostEqual(final_value([[-1, 12, 3], [8], [], [1, -3]]), [3, 8 , -3])
        self.assertListAlmostEqual(final_value([[1,2,3], [4,5], [8,90,12]]), [3,5,12])
        self.assertListAlmostEqual(final_value([[0, -2], [1, 1, 45], []]), [-2, 45])

    #return a 2D list of integers such that each inner list represents the corresponding integers original list number of times
    def test_repeat_value(self):
        self.assertListAlmostEqual(repeat_value([1, 2, 3]), [[1], [2, 2], [3, 3, 3]])
        self.assertListAlmostEqual(repeat_value([0, 4, 2]), [[], [4, 4, 4, 4],[2, 2]])
        self.assertListAlmostEqual(repeat_value([1, 5, 0, 3]), [[1], [5, 5, 5, 5, 5], [], [3, 3, 3]])


if __name__ == '__main__':
    unittest.main()