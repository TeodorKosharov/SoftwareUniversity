initial_list = input().split('!')

while True:
    command = input()
    if command == "Go Shopping!":
        print(', '.join(initial_list))
        break

    command_list = command.split()
    if command_list[0] == 'Urgent':
        if command_list[1] not in initial_list:
            initial_list.insert(0, command_list[1])

    elif command_list[0] == 'Unnecessary':
        if command_list[1] in initial_list:
            initial_list.remove(command_list[1])

    elif command_list[0] == 'Correct':
        if command_list[1] in initial_list:
            initial_list[initial_list.index(command_list[1])] = command_list[2]

    elif command_list[0] == 'Rearrange':
        if command_list[1] in initial_list:
            initial_list.remove(command_list[1])
            initial_list.append(command_list[1])
