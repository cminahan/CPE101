# Lab 5
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101-03

import unittest
from str_funcs import*

class TestCases(unittest.TestCase):

    def test_vowel_extractor(self):
        self.assertEqual(vowel_extractor('hello'), 'eo')
        self.assertEqual(vowel_extractor('banana'), 'aaa')
        self.assertEqual(vowel_extractor('sound'), 'ou')

    def test_str_translate(self):
        self.assertEqual(str_translate('sparkles', 'r', 'a'), 'spaakles')
        self.assertEqual(str_translate('skateboard', 'a', 'z'), 'skztebozrd')
        self.assertEqual(str_translate('pterodactyl', 't', 'H'), 'pHerodacHyl')

    def test_str_rotate(self):
        self.assertEqual(str_rotate('DiNoSaUr'), 'QvAbFnHe')
        self.assertEqual(str_rotate('Hour-Glass'), 'Ubhe-Tynff')
        self.assertEqual(str_rotate('starFish*98'), 'fgneSvfu*98')

    def test_make_substring(self):
        self.assertEqual(make_substring('Test for substring function', 3, 10, 2), 'tfrs')
        self.assertEqual(make_substring('unicorn and rainbow', 4, 16, 4), 'oarb')
        self.assertEqual(make_substring('california polytechnic university', 3, 12, 5), 'ii')

    def test_is_plaindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('anna'))
        self.assertFalse(is_palindrome('broccoliloccobr'))

    def test_count_characters(self):
        self.assertEqual(count_characters('count characters', 'c'), 3)
        self.assertEqual(count_characters('banana broccoli', 'z'), -1)
        self.assertEqual(count_characters('hoppy floppy panda', 'p'), 5)

#Run the test
if __name__ == '__main__':
    unittest.main()