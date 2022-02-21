total_price = 0
total_taxes = 0
total = 0
while True:

    inp = input()

    if inp == 'special' or inp == 'regular':
        break

    price = float(inp)
    if price < 0:
        print('Invalid price!')
        continue

    tax = 0.20 * price
    total_taxes += tax
    total_price += price

total = total_price + total_taxes
if inp == 'special':
    total -= 0.10 * total

if total == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {total_taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total:.2f}$')
