import re

name_pattern = r'(?<=%)[A-Z][a-z]+(?=%)'
product_pattern = r'(?<=<)\w+(?=>)'
quantity_pattern = r'(?<=\|)\d+(?=\|)'
price_pattern = r'\d+(\.)?(\d+)?(?=\$)'

total_sum = 0

while True:
    inp = input()
    if inp == 'end of shift':
        break

    current_name = re.findall(name_pattern, inp)
    if current_name:
        current_name = current_name[0]

    current_product = re.findall(product_pattern, inp)
    if current_product:
        current_product = current_product[0]

    current_quantity = re.findall(quantity_pattern, inp)
    if current_quantity:
        current_quantity = int(current_quantity[0])

    current_price = re.search(price_pattern, inp)
    if current_price:
        current_price = current_price.group()
        if '.' in current_price:
            current_price = float(current_price)
        else:
            current_price = int(current_price)

    if current_name and current_product and current_quantity and current_price:
        print(f'{current_name}: {current_product} - {current_price * current_quantity:.2f}')
        total_sum += current_price * current_quantity

print(f'Total income: {total_sum:.2f}')
