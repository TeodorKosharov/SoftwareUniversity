products = input().split('|')

while True:
    command = input()
    if command == "Shop!":
        break
    command_list = command.split('%')
    if command_list[0] == 'Important':
        if command_list[1] in products:
            products.remove(command_list[1])
            products.insert(0, command_list[1])
        else:
            products.insert(0, command_list[1])

    elif command_list[0] == 'Add':
        if command_list[1] not in products:
            products.append(command_list[1])
        else:
            print("The product is already in the list.")

    elif command_list[0] == 'Swap':
        if command_list[1] in products and command_list[2] in products:
            temp = command_list[2]
            products[products.index(command_list[2])] = command_list[1]
            products[products.index(command_list[1])] = temp

        elif command_list[1] not in products:
            print(f"Product {command_list[1]} missing!")
        elif command_list[2] not in products:
            print(f"Product {command_list[2]} missing!")

    elif command_list[0] == 'Remove':
        if command_list[1] in products:
            products.remove(command_list[1])
        else:
            print(f"Product {command_list[1]} isn't in the list.")

    elif command_list[0] == "Reversed":
        products.reverse()

counter = 1
for element in products:
    print(f'{counter}. {element}')
    counter += 1
