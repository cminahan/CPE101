# Lab 7
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

# List Comprehensions

#Map Patterns

#squares the input value
#int --> int
def square(x):
    x = x**2
    return x

#returns a list with the sqaure of each value in the given list
#list --> list
def square_all(list1):
    list2 = list(map(square, list1))
    return list2

#returns 1 is the input is even and 0 if it's odd
#int --> int
def even_all(x):
    if x%2 == 0:
        return 1
    else:
        return 0

#returns alist containing 0 and 1 representing whether each corresponding integer in teh list is even or odd
#list --> list
def is_even_all(list1):
    list2 = list(map(even_all, list1))
    return list2

#returns a list with n multiplied with each element in the given list
#list int --> list
def mult_with_n(list1, n):
    list2 = [x*n for x in list1]
    return list2

#Filter Patterns

#determines if value negative
#int --> boolean
def negative(x):
    if x < 0:
        return True
    else:
        False

#returns a list of all negative values in the given list
#list --> list
def negative_list(list1):
    list2 = list(filter(negative, list1))
    return list2
print(negative_list([1,-2,3,4,-9]))
#returns a list of value in the given list that are smaller than n
#list --> list
def smaller_than_n(list1, n):
    list2 = [x for x in list1 if x < n]
    return list2

#returns a list of all values in the given list that are between the givend intervals(exclusive)
#list --> list
def between_range(list1, bottom, top):
    list2 = [x for x in list1 if bottom < x < top]
    return list