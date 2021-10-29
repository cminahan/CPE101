# Project 4 - Calcudoku
# Section: CPE101 - 03
# Name: Claire Minahan
# Instructor: S. Einakian

# creates the cages
# input --> list
def create_cages():
    num_of_cages = int(input())
    cages = []
    x = 0
    while x < num_of_cages:
        cage_num = input()
        cage_num = cage_num.split()
        cage_num = [int(y) for y in cage_num]
        cages.append(cage_num)
        x += 1
    return cages

# return true if all rows contain no duplicate numbers, and false otherwise
# list --> boolean
def validate_rows(grid):
    for nest in range(len(grid)):
        for index in range(len(grid[nest])):
            if grid[nest][index] == 0:
                continue

            elif index == 0:
                for x in range(1,5):
                    if grid[nest][index] == grid[nest][x] and grid[nest][x] != 0:
                        return False
            elif index == 1:
                for x in range(2,5):
                    if grid[nest][index] == grid[nest][x] and grid[nest][x] != 0:
                        return False
            elif index == 2:
                for x in range(3, 5):
                    if grid[nest][index] == grid[nest][x] and grid[nest][x] != 0:
                        return False
            elif grid[nest][3] == grid[nest][4] and grid[nest][3] != 0 and grid[nest][4] != 0:
                return False
    return True

# return true if all columns contain no duplicate numbers, and false otherwise
# list --> boolean
def validate_columns(grid):
    for nest in range(len(grid)):
        for index in range(len(grid[nest])):
            if grid[nest][index] == 0:
                continue
            elif index == 0:
                for x in range(1,5):
                    if grid[index][nest] == grid[x][nest] and grid[x][nest] != 0:
                        return False
            elif index == 1:
                for x in range(2,5):
                    if grid[index][nest] == grid[x][nest] and grid[x][nest] != 0:
                        return False
            elif index == 2:
                for x in range(3, 5):
                    if grid[index][nest] == grid[x][nest] and grid[x][nest] != 0:
                        return False
            elif grid[3][nest] == grid[4][nest] and grid[3][nest] != 0 and grid[4][nest] != 0:
                return False
    return True

# return true if the sum of values in a fully populated cage equals the required sum or the sum of values in a
# partially populated cage is less than the required sum and False
# list list --> boolean
def validate_cages(grid, cages):
    for index in cages:
        sum = 0
        for item in range(1, len(index)):
            tot = index[0]
            sum += grid[(index[item])//5][(index[item])%5]
            zero = 0
            if grid[(index[item])//5][index[item]%5] == 0:
                zero = 1
        if zero == 1 and sum < tot:
            continue
        elif sum != tot:
            return False
    return True

# return true if all 3 validation functions return true and false otherwise
# boolean boolean boolean --> boolean
def validate_all(grid, cages):
    if validate_rows(grid) and validate_columns(grid) and validate_cages(grid, cages):
        return True
    return False


