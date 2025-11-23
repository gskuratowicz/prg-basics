###
# A program that calculates the distance to the horizon
# from a height given in meters

import math
h = 1.76 # height of observer in meters
d = 3.57 * math.sqrt(h) # d being distance to the horizon in kilometers, h is the height of the observer in meters
print("The distance to the horizon is", d)