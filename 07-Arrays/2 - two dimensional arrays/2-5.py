# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for row in cinema_seats:
        for item in row:
            total += 1
   return total


def seats_available(seats):
   available_count = 0
   for row in cinema_seats:
      for item in row:
            if item == 'A':
                available_count += 1
   return available_count

def seats_booked(seats):
   booked_count = 0
   for row in cinema_seats:
      for item in row:
            if item == 'B':
                booked_count += 1
   return booked_count

def seat_status(seats, row, place):
    if seats[row-1][place-1] == "A":
        status = "Available"
    elif seats[row-1][place-1] == "B":
        status = "Booked"
    return status

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))
print(len(cinema_seats))