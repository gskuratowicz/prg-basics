categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most_expensive = max(expenses)
most_expensive_index = expenses.index(most_expensive)

print('The most expensive category was', categories[most_expensive_index], ', which was equal to', most_expensive)