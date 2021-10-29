# Lab 5
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101-03

# displays the vowels in a string
# string --> string
def vowel_extractor(str1):
    str2 = ''
    vowels = 'AaEeIiOoUu'
    for index in str1:
        if index in vowels:
            str2 += index
    return str2

# replaces characters in a string with a new character
# string, character, character --> string
def str_translate(str1, old, new):
    str2 = ''
    for index in str1:
        if index == old:
            str2 += new
        else:
            str2 += index
    return str2

# rotate characters with opposite ASCII code number
# string --> string
def str_rotate(str1):
    str2 = ''
    for index in str1:
        if not(65 <= ord(index) <= 90) and not(97 <= ord(index) <= 122):
            str2 += index
        elif ord(index) <= 90:
            if ord(index) < 78:
                str2 += chr(13 + ord(index))
            else:
                str2 += chr(ord(index) - 13)
        else:
            if ord(index) < 110:
                str2 += chr(13 + ord(index))
            else:
                str2 += chr(ord(index) - 13)
    return str2

# takes a section of a string
# string, int, int, int --> string
def make_substring(str1, start, stop, step):
    str2 = ''
    for index in range(len(str1)):
        if start <= index <= stop:
            str2 += str1[index]
            start += step
    return str2

# determines whether a string is a palindrome
# string --> boolean
def is_palindrome(str1):
    tot = 0
    for index in range(len(str1) // 2):
        if str1[index] == str1[len(str1) -(index + 1)]:
            tot += 1
        else:
            tot += 0
    if tot == len(str1) // 2:
        return True
    else:
        return False

# counts how many of a certain character are in a string
# string, character --> int
def count_characters(str1, char):
    tot = 0
    for index in range(len(str1)):
        if str1[index] == char:
            tot += 1
        else:
            tot += 0
    if tot == 0:
        tot = -1
    return tot

