# zeros = int(input())
# zeros_list = [0 for x in range(zeros)]
#
# while True:
#
#     command = input()
#     command_list = command.split()
#
#     if command == 'End':
#         break
#
#     if command_list[0] == 'add':
#         zeros_list[-1] += int(command_list[1])
#
#     elif command_list[0] == 'insert':
#         index = int(command_list[1])
#         zeros_list[index] += int(command_list[2])
#
#     elif command_list[0] == 'leave':
#         index = int(command_list[1])
#         zeros_list[index] -= int(command_list[2])
#
# print(zeros_list)

wagons = [0 for x in range(int(input()))]

command = input()
while command != 'End':

    if command.split()[0] == 'add':
        wagons[-1] += int(command.split()[1])
    elif command.split()[0] == 'insert':
        wagons[int(command.split()[1])] += int(command.split()[2])
    else:
        wagons[int(command.split()[1])] -= int(command.split()[2])
    command = input()

print(wagons)
