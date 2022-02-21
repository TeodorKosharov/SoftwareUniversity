# empty_list = ['x'] * 10
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     command_list = command.split('-')
#     position = int(command_list[0]) - 1
#     job = command_list[1]
#
#     empty_list[position] = job
#
# final_list = [element for element in empty_list if element != 'x']
# print(final_list)


chores = {}

command = input()
while command != 'End':
    chores.update({int(command.split('-')[0]): command.split('-')[1]})
    command = input()

chores = dict(sorted(chores.items(), key=lambda x: x[0]))
print([x for x in chores.values()])
