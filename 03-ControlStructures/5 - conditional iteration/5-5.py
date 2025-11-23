###
# Sums numbers entered by user
#
total_sum = 0
count = -1

while True:
    number = int(input("Enter a number (0 to stop): "))
    count += 1
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean of your numbers is {total_sum / count}")