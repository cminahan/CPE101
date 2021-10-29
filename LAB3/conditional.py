# Lab 3
#
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101 03

#takes two numbers and returns the larger value
#float float --> float
def max_of_2(x, y):
    if x > y:
        return x
    else:
        return y

#takes three numbers and returns the largest value
#float float float --> float
def max_of_3(x, y ,z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

#takes a number(days late) and returns the number of dollars required in the fee
#int --> int
def rental_late_fee(x):
    if x <= 0:
        return 0
    elif x <= 5:
        return 15
    elif x <= 12:
        return 20
    elif x <= 22:
        return 29
    return 100
