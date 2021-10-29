# Lab 3
#
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101 03

#takes a number and returns true if it is odd
#int --> bool
def is_odd(x):
    return x % 2 != 0

#takes a number and returns true if it falls in one of the intervals
#int --> bool
def in_an_interval(x):
    t1 = -5 <= x < 4
    t2 = 12 < x < 52
    t3 = 7 < x <= 10
    t4 = 110 <= x <= 137
    sol = t1 or t2 or t3 or t4
    return sol

#takes 2 numbers and returns true if they both fall their interval, and if the first is divisible to the second
#float float --> bool
def is_divisible_in_interval(x, y):
    res = 25 <= x <= 320
    res1 = 20 < y <= 200
    res2 = x % y == 0
    sol = res and res1 and res2
    return sol


