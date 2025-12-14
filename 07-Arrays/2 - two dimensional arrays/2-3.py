# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_expenses = 0
transport_expenses = 0
utilities_expenses = 0
total = 0

for week in monthly_expenses:
    food_expenses += week[0]
    transport_expenses += week[1]
    utilities_expenses += week[2]

week_1 = sum(monthly_expenses[0])
week_2 = sum(monthly_expenses[1])
week_3 = sum(monthly_expenses[2])
week_4 = sum(monthly_expenses[3])

for row in monthly_expenses:
    for item in row:
        total += item

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food_expenses)
print('Transport:',transport_expenses)
print('Utilities:',utilities_expenses)
print('Week 1:',week_1)
print('Week 2:',week_2)
print('Week 3:',week_3)
print('Week 4:',week_4)
print('---------------')
print('TOTAL:',total)