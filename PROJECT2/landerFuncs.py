# For every function write purpose statement and signature
# Project 2 - Moonlander Functions
# Author: Claire Minahan
# Section: CPE101-03

#displays welcome statement
def showWelcome():
   print("Welcome aboard the Lunar Module Flight Simulator")
   print("")
   print("  To begin you must specify the LM's initial altitude")
   print("  and fuel level. To simulate the actual LM use")
   print("  values of 1300 meters and 500 liters, respectively.")
   print('')
   print("  Good luck and may the force be with you!")

#obtains amount of fuel on board from user
#return int
def getFuelAmount():
   fuel = eval(input("Enter the initial amount of fuel on board the LM (in liters): "))
   wrong = "ERROR: Amount of fuel must be positive, please try again"
   while type(fuel) != int or fuel <= 0:
      print(wrong)
      fuel = eval(input("Enter the initial amount of fuel on board the LM (in liters): "))
   return fuel

#obtains altitude from user
#return int or float
def getAltitude():
   alt = eval(input("Enter the initial altitude of the LM (in meters): "))
   wrong = "ERROR: Altitude must be between 1 and 9999, inclusive, please try again"
   while (type(alt) != int) and (type(alt) != float) or not(1 <= alt <= 9999):
      print(wrong)
      alt = eval(input("Enter the initial altitude of the LM (in meters): "))
   return alt

#shows LM State , shows time, altitude, velocity, fuel, and rate
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print("Elapsed Time: %4d s" % (elapsedTime))
   print("%12s: %4d l" %("Fuel", fuelAmount))
   print("%12s: %4d l/s" %("Rate", fuelRate))
   print("%12s: %7.2f m" %("Altitude", altitude))
   print("%12s: %7.2f m/s" %("Velocity", velocity))

#obtains fuel rate from user
#returns int
def getFuelRate(currentFuel):
   fuel = eval(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   wrong = "ERROR: Fuel rate must be between 0 and 9, inclusive"
   while type(fuel) != int or not(0 <= fuel <= 9):
      print(wrong)
      fuel = eval(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   return fuel

#gets new acceleration
#int float --> float
def updateAcceleration(gravity, fuelRate):
   acc = gravity * ((fuelRate/5)-1)
   return acc

#gets new altitude
#float float float --> float
def updateAltitude(altitude, velocity, acceleration):
   alt = altitude + velocity + (acceleration/2)
   if alt < 0.00:
      return 0.00
   return alt

#gets new velocity
#float float --> float
def updateVelocity(velocity, acceleration):
   vel = velocity + acceleration
   return float(vel)

#gets new fuel amount
def updateFuel(fuelAmount, fuelRate):
   fuel = fuelAmount - fuelRate
   return int(fuel)

def displayLMLandingStatus(velocity):
   if -1 < velocity <= 0:
      print("Status at landing - The eagle has landed!")
   elif -10 < velocity < -1:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <= -10:
      print("Status at landing - Ouch - that hurt!")