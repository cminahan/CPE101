# Lab 4
#
# Name: Claire Minahan
# Instructor: Sussan Einakian
# Section: CPE101-03

import driver

def letter(row, col):
    if row <= 1 or row >= 7:
        return 'T'
    elif row == 2 or row == 3:
        if 4 <= col <= 9:
            return 'Z'
        else:
            return 'T'
    elif row == 4 or row == 5:
        if 4 <= col <= 6:
            return 'Z'
        elif 7 <= col <= 9:
            return 'X'
        elif 10 <= col <= 12:
            return 'B'
        else:
            return 'T'
    elif row == 6:
        if 7 <= col <= 12:
            return 'B'
        else:
            return 'T'

if __name__ == '__main__':
    driver.comparePatterns(letter)
