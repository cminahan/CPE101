# Lab2 Functions

# Name: Claire Minahan

# Section: CPE101 03
from typing import Any, Union

# calculates the solution of equation
# int int --> float
def do_math(x,y):
    doMathSol = ((x**3) + 3 * (y**3)) / ((5 * x) + 7)
    return doMathSol

# calculates solution using + form of quadratic formula
# int int int --> float
def quadratic_formula1(a,b,c):
    quadFormSol1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2 * a)
    return quadFormSol1

# calculates solution using - form of quadratic formula
# int int int --> float
def quadratic_formula2(a,b,c):
    quadFormSol2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2 * a)
    return quadFormSol2

# calculates the distance between two points
# int int int int --> float
def distance(x1, y1, x2, y2):
    distanceSol = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    return distanceSol

# determines whether a number is negative
# int --> boolean
def is_negative(x):
    negativeNum = (x < 0)
    return negativeNum

# determines whether a number is divisable by 7
# int --> boolean
def dividable_by_7(x):
    num = x % 7
    num: bool = bool(num)
    num = not num
    return num