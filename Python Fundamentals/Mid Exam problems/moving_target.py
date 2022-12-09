targets = [int(x) for x in input().split()]

while True:
    command = input()

    if command == 'End':
        break

    command_list = command.split()
    action = command_list[0]
    index = int(command_list[1])

    if action == 'Shoot':
        if 0 <= index <= len(targets) - 1:
            power = int(command_list[2])
            targets[index] -= power

            if targets[index] <= 0:
                targets.pop(index)

    elif action == 'Add':
        if 0 <= index <= len(targets) - 1:
            value = int(command_list[2])
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == 'Strike':
        radius = int(command_list[2])
        if 0 <= index <= len(targets) - 1:
            start_index = index - radius
            end_index = index + radius + 1

            if 0 <= start_index <= len(targets) - 1 and 0 <= end_index <= len(targets) - 1:
                for i in range(start_index, end_index):
                    targets.pop(start_index)
            else:
                print("Strike missed!")

result = [str(x) for x in targets]
print('|'.join(result))
