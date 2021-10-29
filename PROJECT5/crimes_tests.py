# Project 5
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

import unittest
from crimes import*

class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_create_crimes(self):
        test_list = [[234235, 'ROBBERY'], [238523, 'FIRE'], [234234, 'ROBBERY'], [2382934, 'ROBBERY']]
        result_list = [[234234, 'ROBBERY'], [234235, 'ROBBERY'], [2382934, 'ROBBERY']]
        self.assertListAlmostEqual(create_crimes(test_list), result_list)
        test_list2 = [[1098235, 'FIRE'], [92350935, 'ROBBERY'], [1724, 'ROBBERY'], [23984, 'THEFT'], [139834, 'ROBBERY'],
                     [92834923, 'ROBBERY'], [2384, 'MURDER']]
        result_list2 = [[1724, 'ROBBERY'], [139834, 'ROBBERY'], [92350935, 'ROBBERY'], [92834923, 'ROBBERY']]
        self.assertListAlmostEqual(create_crimes(test_list2), result_list2)
        test_list3 = [[2394, 'THEFT'], [2934, 'MURDER'], [29384, 'ROBBERY'], [239478, 'ASSAULT']]
        result_list3 =[[29384, 'ROBBERY']]
        self.assertListAlmostEqual(create_crimes(test_list3), result_list3)

    def test_find_crimes(self):
        test_list = [[234234, 'ROBBERY'], [234235, 'ROBBERY'], [2382934, 'ROBBERY']]
        self.assertEqual(find_crimes(test_list, 234235), 1)
        test_list2 = [[1724, 'ROBBERY'], [139834, 'ROBBERY'], [92350935, 'ROBBERY'], [92834923, 'ROBBERY']]
        self.assertEqual(find_crimes(test_list2, 92350935), 2)
        test_list3 = [[82723, 'ROBBERY'], [287593859723, 'ROBBERY'], [238765, 'ROBBERY'], [9364, 'ROBBERY'], [763748, 'ROBBERY']]
        self.assertEqual(find_crimes(test_list3, 9364), 3)

    def test_update_crimes(self):
        test1 = [[2382374, 'ROBBERY'], [234235, 'ROBBERY'], [2382934, 'ROBBERY']]
        test2 = [[2382374, 'Tuesday', '01/06/2015', '12:35'], [234235, 'Saturday', '12/13/2017', '03:18'], [2382934, 'Thursday', '05/23/2011', '05:19']]
        result1 = [[2382374, 'ROBBERY', 'Tuesday', '01/06/2015', '12:35'], [234235, 'ROBBERY', 'Saturday', '12/13/2017', '03:18'], [2382934, 'ROBBERY', 'Thursday', '05/23/2011', '05:19']]
        self.assertListAlmostEqual(update_crimes(test1, test2), result1)
        test3 = [[3274, 'ROBBERY'], [29274, 'ROBBERY']]
        test4 = [[3274, 'Tuesday', '01/01/2015', '15:00'], [29274, 'Friday', '04/13/2012', '00:01']]
        result2 = [[3274, 'ROBBERY', 'Tuesday', '01/01/2015', '15:00'], [29274, 'ROBBERY', 'Friday', '04/13/2012', '00:01']]
        self.assertListAlmostEqual(update_crimes(test3, test4), result2)
        test5 = [[23746, 'ROBBERY'], [73934, 'ROBBERY']]
        test6 = [[23746, 'Monday', '02/24/2008', '09:30'], [73934, 'Saturday', '02/13/2015', '14:33']]
        result3 = [[23746, 'ROBBERY', 'Monday', '02/24/2008', '09:30'], [73934, 'ROBBERY', 'Saturday', '02/13/2015', '14:33']]
        self.assertListAlmostEqual(update_crimes(test5, test6), result3)

    def test_count_crimes(self):
        test1 = [[234234, 'ROBBERY', 'Saturday', '12', '03'], [234235, 'ROBBERY', 'Saturday', '12', '15'],[2382934, 'ROBBERY', 'Thursday', '05', '15']]
        result1 = 'NUMBER OF PROCESSED ROBBERIES: 3 \nDAY WITH MOST ROBBERIES: Saturday\nMONTH WITH MOST ROBBERIES: December\nHOUR WITH MOST ROBBERIES: 3PM'
        self.assertAlmostEqual(count_crimes(test1), result1)
        test2 = [[3274, 'ROBBERY', 'Tuesday', '01', '15'], [29274, 'ROBBERY', 'Friday', '04', '00'], [28493, 'ROBBERY', 'Friday', '01', '15']]
        result2 = 'NUMBER OF PROCESSED ROBBERIES: 3 \nDAY WITH MOST ROBBERIES: Friday\nMONTH WITH MOST ROBBERIES: January\nHOUR WITH MOST ROBBERIES: 3PM'
        self.assertAlmostEqual(count_crimes(test2), result2)
        test3 = [[23746, 'ROBBERY', 'Monday', '02', '09'], [73934, 'ROBBERY', 'Saturday', '02', '14'], [84338, 'ROBBERY', 'Saturday', '11', '14']]
        result3 = 'NUMBER OF PROCESSED ROBBERIES: 3 \nDAY WITH MOST ROBBERIES: Saturday\nMONTH WITH MOST ROBBERIES: November\nHOUR WITH MOST ROBBERIES: 2PM'
        self.assertAlmostEqual(count_crimes(test3), result3)

    def test_crime_objects(self):
        crime1 = Crime(8239583, 'ROBBERY')
        crime1.set_time('Monday', '02', '09')
        crime2 = Crime(928373, 'ARSON')
        crime2.set_time('Tuesday', '12', '23')
        self.assertTrue(crime1 != crime2)
        crime3 = Crime(83484, 'THEFT')
        crime3.set_time('Wednesday', '11', '00')
        crime4 = Crime(83484, 'PUBLIC INDECENCY')
        crime4.set_time('Saturday', '09', '20')
        self.assertTrue(crime3 == crime4)

if __name__ == '__main__':
    unittest.main()