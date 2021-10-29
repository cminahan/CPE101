# Lab 6: Polynomial Functions Test
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

# Filter Pattern

# returns a list of all even values in the input list
# list --> list
def are_even(list1):
    list2 = [x for x in list1 if x%2 == 0]
    return list2

#print(are_even([2, 4, 7]))

# returns a new list removing the duplicate
# list --> list
def remove_duplicates(list1):
    list2 = []
    for item in list1:
        if item not in list2:
            list2.append(item)
    return list2

# returns a new list of all values divisable by n in the input list
# list int --> list
def are_divisable_by_n(list1, n):
    x = 0
    list2 = []
    while x <= len(list1) - 1:
        if list1[x]%n == 0:
            list2.append(list1[x])
        x += 1
    return list2

