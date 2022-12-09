def index_checker(given_index: int, sequence: str):
    if 0 <= given_index <= len(sequence) - 1:
        return True
    return False


initial_string = input()

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {initial_string}")
        exit()

    command_list = command.split(':')
    action = command_list[0]

    if action == 'Add Stop':
        index = int(command_list[1])
        given_string = command_list[2]
        if index_checker(index, initial_string):
            initial_string = initial_string[:index] + given_string + initial_string[index:]
        print(initial_string)

    elif action == 'Remove Stop':
        start_index = int(command_list[1])
        end_index = int(command_list[2])

        if index_checker(start_index, initial_string) and index_checker(end_index, initial_string):
            #for removing_char in range(start_index, end_index + 1):
                #initial_string = initial_string.replace(initial_string[start_index], '', 1)

            initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
        print(initial_string)

    elif action == 'Switch':
        old_string = command_list[1]
        new_string = command_list[2]
        if old_string in initial_string:
            initial_string = initial_string.replace(old_string, new_string)
        print(initial_string)
