# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

#point class
class Point:
    #constructor
    def __init__(self, xcoor, ycoor):
        self.x = xcoor
        self.y = ycoor

    #boilerplate
    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return type(self) == type(other) and\
               self.x == other.x and\
               self.y == other.y

#circle class
class Circle:
    #constructor
    def __init__(self, centPoint, radius):
        self.center = centPoint
        self.r = radius

    #boilerplate
    def __repr__(self):
        return'center: {}, radius: {:.2f}'.format(self.center, self.r)

    def __eq__(self, other):
        return type(self) == type(other) and\
               self.center.x == other.center.x and\
               self.center.y == other.center.y and\
               self.r == other.r

