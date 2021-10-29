# Lab 9
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

from objects import*

# returns the distance between two points
#point point --> float
def distance(point1, point2):
    dist = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**(1/2)
    return dist

# returns True when the circles overlap and False otherwise
# obj obj --> boolean
def circle_overlap(circle1, circle2):
    dist = distance(circle1.center, circle2.center)
    sum = circle1.r + circle2.r
    return dist < sum
