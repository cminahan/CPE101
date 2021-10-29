# Lab 8
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

# File Input

#for each line in the file, pring the number, number of characters in the line, and the line itself
#none --> string
def txt():
    fin = open('in.txt', 'r')
    x = 0
    for line in fin:
        print('Line  %d  (%d chars): %s' %(x, len(line)-1, line))
        x += 1
    fin.close()

txt()