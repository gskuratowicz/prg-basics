price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
total = 0
for product,price in price_list.items():
    print(f'The price for product {product} before discount is {price}.')
    total += price
print("The total price for all products before discount is: ",round(total,2))

for product,price in price_list.items():
    price_list[product] = round(price * 0.9, 2)


total = 0
for product,price in price_list.items():
    print(f'The price for product {product} after discount is {price}.')
    total += price
print("The total price for all products after discount is: ",round(total,2))


