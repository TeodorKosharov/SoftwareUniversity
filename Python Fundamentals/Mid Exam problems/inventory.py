journal = input().split(', ')

while True:
    command = input()
    if command == "Craft!":
        print(', '.join(journal))
        break
    command_list = command.split(' - ')
    if command_list[0] == 'Collect':
        if command_list[1] not in journal:
            journal.append(command_list[1])
    elif command_list[0] == 'Drop':
        if command_list[1] in journal:
            journal.remove(command_list[1])
    elif command_list[0] == 'Combine Items':
        if command_list[1].split(':')[0] in journal:
            journal.insert(journal.index(command_list[1].split(':')[0]) + 1, command_list[1].split(':')[1])
    else:
        if command_list[1] in journal:
            journal.append(journal.pop(journal.index(command_list[1])))
