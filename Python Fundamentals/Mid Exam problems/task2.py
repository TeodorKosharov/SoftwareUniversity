sequence = list(map(int, input().split()))

while True:
    command = input()
    if command == "END":
        print(', '.join(list(map(str, sequence))))
        break
    command_list = command.split()
    if ' '.join(command_list[:3]) == 'add to start':
        sequence = [int(x) for x in command_list[3:]] + sequence

    elif ' '.join(command_list[:3]) == 'remove greater than':
        sequence = [int(x) for x in sequence if x <= int(command_list[3])]

    elif command_list[0] == 'replace':
        if int(command_list[1]) in sequence:
            sequence[sequence.index(int(command_list[1]))] = int(command_list[2])

    elif ' '.join(command_list[:3]) == 'remove at index':
        if 0 <= int(command_list[3]) <= len(sequence) - 1:
            sequence.pop(int(command_list[3]))

    elif ' '.join(command_list[:2]) == "find even":
        print(' '.join(list(map(str, [int(x) for x in sequence if x % 2 == 0]))))

    elif ' '.join(command_list[:2]) == 'find odd':
        print(' '.join(list(map(str, [int(x) for x in sequence if x % 2 == 1]))))
