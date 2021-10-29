# Lab 8
# Section: CPE101-03
# Name: Claire Minahan
# Instructor: S. Einakian

# Image File Format

#open and read the file
#none --> none
def open_file():
    fin = open('hidden.ppm', 'r')
    fin.readlines()
    fin.close()

#turn the file into a list
#none --> list
def make_list():
    fin = open('hidden.ppm', 'r')
    list1 = []
    x = 0
    for lines in fin:
        list1.append(lines)
    fin.close()
    return list1

#edit the pixels
#list --> none
def discover(list1):
    fout = open('discover.ppm', 'w')
    x = 0
    y = 0
    red_val = ''
    for line in list1:
        if y < 3:
            y += 1
            fout.write(line)
        else:
            x += 1
            if x == 1:
                val = int(line)
                val *= 10
                if val > 255:
                    val = 255
                red_val = str(val)
                fout.write(red_val)
                fout.write('\n')
            elif x == 2:
                fout.write(red_val)
                fout.write('\n')
            elif x == 3:
                fout.write(red_val)
                fout.write('\n')
                red_val = int(red_val)
                red_val = 0
                x = 0
    fout.close()

discover(make_list())