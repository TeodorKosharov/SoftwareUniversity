# products = input()
# budget = float(input())
#
# products_list = products.split('|')
#
# clothes_max_price = 50
# shoes_max_price = 35
# accessories_max_price = 20.50
#
# is_bought_successful = False
# bought_items_list = []
# profit = 0
# new_budget = 0
# total_increased_prices = 0
#
# for element in products_list:
#
#     cell_list = element.split('->')
#     product_type = cell_list[0]
#     product_price = float(cell_list[1])
#
#     if budget < product_price:
#         continue
#
#     if product_type == 'Clothes' and product_price <= clothes_max_price:
#         budget -= product_price
#         is_bought_successful = True
#
#     elif product_type == 'Shoes' and product_price <= shoes_max_price:
#         budget -= product_price
#         is_bought_successful = True
#
#     elif product_type == 'Accessories' and product_price <= accessories_max_price:
#         budget -= product_price
#         is_bought_successful = True
#
#     else:
#         is_bought_successful = False
#
#     if is_bought_successful:
#         increased_price = product_price + 0.40 * product_price
#         total_increased_prices += increased_price
#         bought_items_list.append(increased_price)
#         profit += (increased_price - product_price)
#
# total_budget = total_increased_prices + budget
#
# for element in bought_items_list:
#     print(f'{element:.2f}', end=' ')
#
# print()
# print(f'Profit: {profit:.2f}')
#
# if total_budget >= 150:
#     print('Hello, France!')
# else:
#     print("Not enough money.")


products = input().split('|')
budget = float(input())

bought_items_prices = []
profit = 0

for product in products:
    product_data = product.split('->')

    if product_data[0] == 'Clothes' and float(product_data[1]) <= 50 and float(product_data[1]) <= budget:
        budget -= float(product_data[1])
        profit += float(product_data[1]) + 0.40 * float(product_data[1]) - float(product_data[1])
        bought_items_prices.append(format(float(product_data[1]) + 0.40 * float(product_data[1]), '.2f'))

    elif product_data[0] == 'Shoes' and float(product_data[1]) <= 35 and float(product_data[1]) <= budget:
        budget -= float(product_data[1])
        profit += float(product_data[1]) + 0.40 * float(product_data[1]) - float(product_data[1])
        bought_items_prices.append(format(float(product_data[1]) + 0.40 * float(product_data[1]), '.2f'))

    elif product_data[0] == 'Accessories' and float(product_data[1]) <= 20.50 and float(product_data[1]) <= budget:
        budget -= float(product_data[1])
        profit += float(product_data[1]) + 0.40 * float(product_data[1]) - float(product_data[1])
        bought_items_prices.append(format(float(product_data[1]) + 0.40 * float(product_data[1]), '.2f'))

budget += sum(list(map(float, bought_items_prices)))

print(' '.join(list(map(str, bought_items_prices))))
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
