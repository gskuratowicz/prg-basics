###
# A program that calculates the distance to the horizon
# from a height given in meters

import math
h = 20
d = 3.57 * math.sqrt(h) # d being distance to the horizon in kilometers, h is the height of the observer in meteres
print("The distance to the horizon is", d)