journal = input().split(', ')

while True:
    command = input()

    if command == 'Craft!':
        print(', '.join(journal))
        break

    command_list = command.split(' - ')

    if command_list[0] == 'Collect':
        item = command_list[1]

        if item not in journal:
            journal.append(item)

    elif command_list[0] == 'Drop':
        item = command_list[1]

        if item in journal:
            journal.remove(item)

    elif command_list[0] == 'Combine Items':
        items = command_list[1].split(':')
        old_item = items[0]
        new_item = items[1]

        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)

    elif command_list[0] == 'Renew':
        item = command_list[1]

        if item in journal:
            journal.remove(item)
            journal.append(item)
