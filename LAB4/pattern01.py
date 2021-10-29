# Lab 4
#
# Name: Claire Minahan
# Instructor: Sussan Einakian
# Section: CPE101-03

import driver


def letter(row, col):
    if (row == 9 and col == 9):
        return 'Z'
    else:
        return 'G'


if __name__ == '__main__':
    driver.comparePatterns(letter)
