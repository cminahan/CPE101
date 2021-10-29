# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

#check equality of two float value
#float float --> boolean
def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

#Point class
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
               self.y == other.y and\
               epsilon_equal(self.x, other.x) and\
               epsilon_equal(self.y, other.y)

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
               self.center == other.center and\
               self.r == other.r


