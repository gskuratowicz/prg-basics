circumference = float(input('Enter circumference of tree in cm: '))

can_be_cut_down = (circumference / 3.14159) >= 50
print(f'Tree can be cut down: {can_be_cut_down}')