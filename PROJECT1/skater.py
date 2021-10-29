# Project 1
#
# Name: Claire Minahan
# Instructor: S. Einakian
# Section: CPE101-03

from projFuncs import*
def main():
    # Inputs
    pounds = input('How much do you weigh (pounds)? ')
    pounds = float(pounds)
    profDistance = input('How far away is your professor (meters)? ')
    profDistance = float(profDistance)
    object = input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome?')

    # Calculations
    weight = convertPoundsToKG(pounds)
    objectMass = getMassOfObject(object)
    objectVelocity = getVelocityOfObject(profDistance)
    skaterVelocity = getVelocityOfSkater(weight, objectMass, objectVelocity)
    skaterV = ('%.3f'%skaterVelocity)

    # Response
    if objectMass <= 0.1:
        print("Nice throw! You're going to get an F!")
    elif 0.1 < objectMass <= 1.0:
        print("Nice throw! Make sure your professor is OK.")
    elif objectMass > 1.0:
        if profDistance < 20:
            print("Nice throw! How far away is the hospital?")
        else:
            print("Nice throw! RIP professor")

    print('Velocity of skater: ' + skaterV + ' m/s')

    if skaterVelocity < 0.2:
        print("My grandmother skates faster than you")
    elif skaterVelocity >= 1.0:
        print("Look out for that railing!!!")


#Run the main test
if __name__ == '__main__':
   main()