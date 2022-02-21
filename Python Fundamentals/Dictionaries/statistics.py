# all_products = {}
#
# while True:
#     command = input()
#     if command == 'statistics':
#         break
#
#     product = command.split(': ')
#     key = product[0]
#     value = int(product[1])
#
#     if key in all_products.keys():
#         all_products[key] += value
#     else:
#         all_products[key] = value
#
# print('Products in stock:')
# for element in all_products:
#     print(f'- {element}: {all_products[element]}')
# print(f'Total Products: {len(all_products.keys())}')
# print(f'Total Quantity: {sum(all_products.values())}')


products = {}

while True:
    inp = input().split(': ')
    if inp[0] == 'statistics':
        break

    if inp[0] not in products:
        products.update({inp[0]: int(inp[1])})
    else:
        products[inp[0]] += int(inp[1])

print("Products in stock:")
for food, quantity in products.items():
    print(f"- {food}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
