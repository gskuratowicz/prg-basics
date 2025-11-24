###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    user_input = abs(any_number)
    user_input_as_str = str(user_input)
    for char in user_input_as_str:
        digit = int(char)
        sum += digit

    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')