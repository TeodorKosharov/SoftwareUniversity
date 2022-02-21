given_string = input()

while True:
    command = input()
    if command == 'End':
        break

    command_list = command.split(' ')

    if command_list[0] == 'Translate':
        given_string = given_string.replace(command_list[1], command_list[2])
        print(given_string)

    elif command_list[0] == 'Includes':
        if command_list[1] in given_string:
            print('True')
        else:
            print('False')

    elif command_list[0] == 'Start':
        substring = command_list[1]
        print(given_string.startswith(substring))

    elif command_list[0] == 'Lowercase':
        given_string = given_string.lower()
        print(given_string)

    elif command_list[0] == 'FindIndex':
        print(given_string.rfind(command_list[1]))

    elif command_list[0] == 'Remove':
        start_index = int(command_list[1])
        end_index = start_index + int(command_list[2])
        given_string = given_string[:start_index] + given_string[end_index:]
        print(given_string)
