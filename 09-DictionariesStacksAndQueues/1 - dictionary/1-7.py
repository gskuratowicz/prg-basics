products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

i = 1
total = 0
for name,amount in products.items():
    print(f'{i}. {name} quantity: {amount}')
    i += 1
    total += amount

print("The total amount of products in the store is ",total)