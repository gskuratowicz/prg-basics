###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

number_of_seconds = int(input("Enter the number of seconds to count down: "))

while number_of_seconds > 0:
    if number_of_seconds > 5:
        print(number_of_seconds)
    elif number_of_seconds == 5:
        print('five')
    elif number_of_seconds == 4:
        print('four')
    elif number_of_seconds == 3:
        print('three')
    elif number_of_seconds == 2:
        print('two')
    elif number_of_seconds == 1:
        print('one')
    number_of_seconds -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")
