# Project 4 - Word Puzzle
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: 101-03

#makes the rows of the string into lists
#string --> list(list)
def make_rows(string1):
    row1 = [string1[num] for num in range(10)]
    row2 = [string1[num] for num in range(10, 20)]
    row3 = [string1[num] for num in range(20, 30)]
    row4 = [string1[num] for num in range(30, 40)]
    row5 = [string1[num] for num in range(40, 50)]
    row6 = [string1[num] for num in range(50, 60)]
    row7 = [string1[num] for num in range(60, 70)]
    row8 = [string1[num] for num in range(70, 80)]
    row9 = [string1[num] for num in range(80, 90)]
    row10 = [string1[num] for num in range(90, 100)]
    rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]
    return rows

#makes the columns of the string into lists
#string --> list(list)
def make_columns(string1):
    col1 = [string1[num] for num in range(0, 100) if num % 10 == 0]
    col2 = [string1[num] for num in range(0, 100) if (num - 1) % 10 == 0]
    col3 = [string1[num] for num in range(0, 100) if (num - 2) % 10 == 0]
    col4 = [string1[num] for num in range(0, 100) if (num - 3) % 10 == 0]
    col5 = [string1[num] for num in range(0, 100) if (num - 4) % 10 == 0]
    col6 = [string1[num] for num in range(0, 100) if (num - 5) % 10 == 0]
    col7 = [string1[num] for num in range(0, 100) if (num - 6) % 10 == 0]
    col8 = [string1[num] for num in range(0, 100) if (num - 7) % 10 == 0]
    col9 = [string1[num] for num in range(0, 100) if (num - 8) % 10 == 0]
    col10 = [string1[num] for num in range(0, 100) if (num - 9) % 10 == 0]
    cols = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10]
    return cols

#searches for a word in the the rows going forward
#list string --> boolean string
def find_horizontal_forward(rows, word):
    length = len(word)
    final = 11 - length
    tot = 0
    start = 0
    no = "not in puzzle"
    for row in range(10):
        for index in range(final):
            if rows[row][index] == word[0]:
                start = index
                for num in range(length):
                    if rows[row][index + num] == word[num]:
                        tot += 1
                if tot == length:
                    return True, "%s: (FORWARD)  row:  %2d    column:  %2d" %(word, row, start)
                else:
                    tot = 0
                    start = 0
    if start == 0:
        return False, no

#searches for a word in the rows going backwards
#list string --> boolean string
def find_horizontal_backwards(rows, word):
    length = len(word)
    final = 11 - length
    tot = 0
    start = 0
    no = 'not in puzzle'
    for row in range(10):
        for index in range(final):
            if rows[row][9-index] == word[0]:
                start = 9 - index
                for num in range(length):
                    if rows[row][9 - index - num] == word[num]:
                        tot += 1
                if tot == length:
                    return True, "%s: (BACKWARD) row: %2d    column: %2d" %(word, row, start)
                else:
                    start = 0
                    tot = 0
    if start == 0:
        return False, no

#searches for a word in the columns going forward
#list string --> boolean string
def find_vertical_down(cols, word):
    length = len(word)
    final = 11 - length
    tot = 0
    start = 0
    no = "not in puzzle"
    for row in range(10):
        for column in range(final):
            if cols[row][column] == word[0]:
                start = column
                for num in range(length):
                    if cols[row][column + num] == word[num]:
                        tot += 1
                if tot == length:
                    return True, "%s: (DOWN) row:  %2d    column:  %2d" %(word, start, row)
                else:
                    tot = 0
                    start = 0
    if start == 0:
        return False, no

#searches for a word in the columns going backwards
#list string --> boolean string
def find_vertical_up(cols, word):
    length = len(word)
    final = 11 - length
    tot = 0
    start = 0
    no = 'not in puzzle'
    for row in range(10):
        for column in range(final):
            if cols[row][9-column] == word[0]:
                start = 9 - column
                for num in range(length):
                    if cols[row][9 - column - num] == word[num]:
                        tot += 1
                if tot == length:
                    return True, "%s: (UP) row: %2d    column: %2d" %(word, start, row)
                else:
                    start = 0
                    tot = 0
    if start == 0:
        return False, no

