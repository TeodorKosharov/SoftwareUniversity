# names_of_gifts = input()
#
# list_of_gifts = names_of_gifts.split()
#
# while True:
#
#     command = input()
#
#     if command == "No Money":
#         break
#
#     elif "OutOfStock" in command:
#         out_of_stock_list = command.split()
#         gift = out_of_stock_list[1]
#
#         for index in range(len(list_of_gifts)):
#
#             if list_of_gifts[index] == gift:
#                 list_of_gifts[index] = 'None'
#
#     elif "Required" in command:
#         required_list = command.split()
#         gift = required_list[1]
#         index = int(required_list[2])
#
#         if 0 <= index < len(list_of_gifts) - 1:
#             list_of_gifts[index] = gift
#
#     elif 'JustInCase' in command:
#         just_in_case_list = command.split()
#         gift = just_in_case_list[1]
#
#         list_of_gifts[-1] = gift
#
# final_list = []
#
# for element in list_of_gifts:
#
#     if element != 'None':
#         final_list.append(element)
#
# print(' '.join(final_list))


gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command_list = command.split()

    if command_list[0] == 'OutOfStock':
        for index in range(len(gifts)):
            if gifts[index] == command_list[1]:
                gifts[index] = None

    elif command_list[0] == 'Required':
        if 0 <= int(command_list[2]) <= len(gifts) - 1:
            gifts[int(command_list[2])] = command_list[1]

    else:
        gifts[-1] = command_list[1]

print(' '.join([x for x in gifts if x is not None]))
