sequence = list(map(int, input().split()))

while True:
    command = input()
    if command == 'end':
        print(', '.join(list(map(str, sequence))))
        break

    command_list = command.split()
    if command_list[0] == 'swap':
        element = sequence[int(command_list[1])]
        sequence[int(command_list[1])] = sequence[int(command_list[2])]
        sequence[int(command_list[2])] = element

    elif command_list[0] == 'multiply':
        sequence[int(command_list[1])] *= sequence[int(command_list[2])]

    else:
        sequence = [x - 1 for x in sequence]