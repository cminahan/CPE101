# Lab 7
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

#group elements from input list into groups of 3
#list --> list
def groups_of_3(list1):
    list2 = []
    num = (len(list1) // 3)
    if len(list1)%3 != 0:
        num += 1
    for x in range(num):
        list2.append([])
    y = 0
    x = 0
    while x < len(list1):
        list2[y].append(list1[x])
        if (x+1)%3 == 0:
            y += 1
        x += 1
    return list2

#return a list that contains only the final element of each inner list from the given list
#list --> list
def final_value(list1):
    list2 = []
    for x in range(len(list1)):
        if len(list1[x]) != 0:
            list2.append(list1[x][len(list1[x])-1])
    return list2

#return a 2D list of integers such that each inner list repeats the corresponding integer in the original list that number of time
#list --> list
def repeat_value(list1):
    list2 = []
    num = len(list1)
    for x in range(num):
        list2.append([])
    for x in range(len(list1)):
            for count in range(list1[x]):
                list2[x].append(list1[x])
    return list2
