price = float(input('What is the price of the product in euros?'))
new_price = price - (price * 5 / 100)
print('The product that cost {:.2f} euros, now with the promotion costs {:.2f} euros'.format(price, new_price))