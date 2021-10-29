# Project 4 - Calcudoku
# Section: CPE101 - 03
# Name: Claire Minahan
# Instructor: S. Einakian

from funcs import*

def main():
    cages = create_cages()
    grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    backtrack = 0
    check = 0

    i = 0
    while i < 25:
        grid[i//5][i%5] += 1
        check += 1
        if validate_all(grid, cages) == True:
            i += 1
        elif grid[i//5][i%5] == 5 and validate_all(grid, cages) == False:
            grid[i//5][i%5] = 0
            i -= 1
            backtrack += 1
            while grid[i//5][i%5] == 5:
                grid[i//5][i%5] = 0
                i -= 1
                backtrack +=1
        elif grid[i//5][i%5] > 5:
            break
    for x in grid:
        for y in x:
            print(y, end = ' ')
        print('')


if __name__ == '__main__':
    main()
