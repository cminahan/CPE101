# Lab 6: Polynomial Functions Test
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian


# Map Pattern

# returns cube of each value in the input list
# list --> list
def cube_all(list1):
    list2 = [x**3 for x in list1]
    return list2

# returns sum of each value and n
# list int --> list
def add_n_to_all(list1, n):
    list2 = []
    x = 0
    while x <= len(list1) - 1:
        list2.append(list1[x] + n)
        x += 1
    return list2

# returns whether or not each value is divisable by 5
# list --> list
def div_by_5_all(list1):
    list2 = []
    for x in list1:
        if x%5 == 0:
            list2.append('True')
        else:
            list2.append('False')
    return list2

