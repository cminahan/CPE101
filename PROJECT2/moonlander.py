# Project 2- Moonlander
# Author: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

from landerFuncs import*

def main():
   showWelcome()

   time = 0
   alt = getAltitude()
   fuel = getFuelAmount()
   vel = 0.00
   rate = 0
   gravity = 1.62
   print('')
   print("LM state at retrorocket cutoff")
   displayLMState(time, alt, vel, fuel, rate)

   while fuel > 0 and alt > 0.00:
       print('')
       rate = getFuelRate(fuel)
       fuel = updateFuel(fuel, rate)
       acc = updateAcceleration(gravity, rate)
       alt = updateAltitude(alt, vel, acc)
       vel = updateVelocity(vel, acc)
       time += 1

       if fuel <= 0:
           rate = 0
           time-= 1
           fuel = 0
           vel = updateVelocity(vel, acc)
           acc = updateAcceleration(gravity, rate)
           while alt > 0:
               time += 1
               print('OUT OF FUEL - Elapsed Time: %4d   Altitude: %8.2f   Velocity: %8.2f' %(time, alt, vel))
               acc = updateAcceleration(gravity, rate)
               alt = updateAltitude(alt, vel, acc)
               vel = updateVelocity(vel, acc)
           time += 1
       if alt == 0:
           print('')
           print("LM state at landing/impact")
       displayLMState(time, alt, vel, fuel, rate)
       if alt == 0 or fuel == 0:
           displayLMLandingStatus(updateVelocity(vel, acc))

if __name__ == "__main__":
   main()

