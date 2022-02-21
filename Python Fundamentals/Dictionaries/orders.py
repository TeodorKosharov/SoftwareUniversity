# products = {}
#
# while True:
#     command = input()
#     if command == "buy":
#         break
#
#     command_list = command.split(' ')
#     name = command_list[0]
#     price = float(command_list[1])
#     quantity = int(command_list[2])
#
#     if name not in products:
#         products[name] = [price, quantity]
#     else:
#         mini_list = products[name]
#         mini_list[1] += quantity
#         if price != mini_list[0]:
#             mini_list[0] = price
#
# for element in products:
#     mini_list = products[element]
#     total_price = mini_list[0] * mini_list[1]
#     print(f'{element} -> {total_price:.2f}')

products = {}
while True:
    command = input()
    if command == 'buy':
        break

    if command.split()[0] not in products:
        products.update({command.split()[0]: [float(command.split()[1]), int(command.split()[2])]})
    else:
        products[command.split()[0]][0] = float(command.split()[1])
        products[command.split()[0]][1] += int(command.split()[2])

for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
