# Lab 6: Polynomial Functions Test
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

#Product

# takes a nested list returns a list of integers such that each integer is a product of its inner list
# list --> list
def product(list1):
    tot = 1
    list2 = []
    for i in range(len(list1)):
        for j in list1[i]:
            tot *= j
        list2.append(tot)
        tot = 1
    return list2
