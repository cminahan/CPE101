# Project 4 - Word Puzzle
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: 101-03

from wordFuncs import*

def main():
    #user input 100 character string and words to find within
    puzzle = input('')
    words1 = input('')
    #turn string into a list
    words = words1.split()

    #create the rows and columns of the puzzle
    cols = make_columns(puzzle)
    rows = make_rows(puzzle)

    #display the 10 x 10 puzzle
    print("Puzzle:")
    print(' ')
    for x in range(10):
        if x == 0:
            print(puzzle[0:10])
        else:
            print(puzzle[x * 10: (x * 10) + 10])
    print(' ')

    #search for the words' locations
    for word in words:
        forward = find_horizontal_forward(rows, word)
        backward = find_horizontal_backwards(rows, word)
        up = find_vertical_up(cols, word)
        down = find_vertical_down(cols, word)
        nope = '%s: word not found' % (word)
        if forward[0] == True:
            print (forward[1])
        elif backward[0] == True:
            print (backward[1])
        elif up[0] == True:
            print (up[1])
        elif down[0] == True:
            print (down[1])
        else:
            print (nope)


if __name__ == "__main__":
   main()

