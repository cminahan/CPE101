# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

#check equality of two float value
#float float --> boolean
def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

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
               self.y == other.y and \
               epsilon_equal(self.x, other.x) and \
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

#determines distance between point and origin
#point point --> float
def distance(point1, point2 = Point(0,0)):
    dist = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**(1/2)
    return dist

#create list of distance of points from origin
#list --> list
def distance_all(list1):
    newL = list(map(distance, list1))
    return newL

#determines if a point is in the first quadrant
#obj --> boolean
def quadrant(point1):
    if point1.x > 0 and point1.y > 0:
        return True
    return False

#returns points in a list that are in the first quadrant
#list --> list
def are_in_first_quadrant(list1):
    newL = list(filter(quadrant, list1))
    return newL
