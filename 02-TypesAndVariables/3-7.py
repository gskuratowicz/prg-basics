###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
north_percentage = north / total * 100
south_percentage = south / total * 100
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("The percentage of people living in % in the northern hemisphere is", north_percentage)
print("The percentage of people living in % in the southern hemisphere is", south_percentage)
