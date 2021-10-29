# Lab 4
#
# Name: Claire Minahan
# Instructor: Sussan Einakian
# Section: CPE101-03

import driver

def letter(row, col):

    if row > 0:
        if col <= (row - 1):
            return 'T'
        else:
            return 'W'
    else:
        return 'W'

if __name__ == '__main__':
    driver.comparePatterns(letter)
