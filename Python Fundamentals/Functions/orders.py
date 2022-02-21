coffee_price = 1.50
water_price = 1
coke_price = 1.40
snacks_price = 2


def function(product, quantity):
    if product == 'coffee':
        return format(quantity * coffee_price, '.2f')
    elif product == 'water':
        return format(quantity * water_price, '.2f')
    elif product == 'coke':
        return format(quantity * coke_price, '.2f')
    elif product == 'snacks':
        return format(quantity * snacks_price, '.2f')


product_inp = input()
quantity_inp = int(input())

result = function(product_inp, quantity_inp)
print(result)
