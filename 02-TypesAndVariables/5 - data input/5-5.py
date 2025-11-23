price = float(input('enter price before discount: '))
discount = float(input('enter the discount in %: ')) / 100
discounted_product_price = round(price - price * discount,2)
difference_between_and_after = round(price - discounted_product_price,2)
print(f'price with discount is {discounted_product_price}.')
print(f'reduction is {difference_between_and_after}.')