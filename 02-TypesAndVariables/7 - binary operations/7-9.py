import random
number_rolled = random.randint(1,6)
special_number = (number_rolled == 1 or number_rolled == 6)
print(f'The number rolled is: {number_rolled}')
print(f'Special number(1 or 6): {special_number}')