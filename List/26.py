#write a program that asks for the price of 3 products, then recommends the cheapest one
products = []
product1 = float(input('Insert the price of the first product: '))
products.append(product1)
product2 = float(input('Insert the price of the second product: '))
products.append(product2)
product3 = float(input('Insert the price of the third product: '))
products.append(product3)
if min(products) == product1:
    print('You should buy the first product for %.2f!' % (product1))
elif min(products) == product2:
    print('You should buy the second product for %.2f!' % (product2))
elif min(products) == product3:
    print('You should buy the third product for %.2f!' % (product3))