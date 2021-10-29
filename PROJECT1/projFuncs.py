# Project 1
#
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101-03

from math import*

# takes an input weight in pounds and returns equivalent mass in KG
# int --> float
def convertPoundsToKG(pounds):
    return pounds * 0.453592

# takes an input representing an object and returns the mass of the object(kg)
# string --> float
def getMassOfObject (object_type):
    if object_type == 't':
        return 0.1
    elif object_type == 'p':
        return 1.0
    elif object_type == 'r':
        return 3.0
    elif object_type == 'g':
        return 5.3
    elif object_type == 'l':
        return 9.07
    return 0.0

# takes the distance of the professor(m) and calculates the velocity of the object
# int --> float
def getVelocityOfObject(distance):
    return sqrt((9.8 * distance) / 2)

# takes the mass of the skater, mass of object, and velocity of object to return
# the velocity of the skater
# int int int --> float
def getVelocityOfSkater(massOfSkater, massOfObject, velocityOfObject):
    return (massOfObject * velocityOfObject) / massOfSkater