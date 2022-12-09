initial_string = input()

while True:
    command = input()
    if command == 'Done':
        print(f"Your password is: {initial_string}")
        break

    command_list = command.split(' ')
    action = command_list[0]

    if action == "TakeOdd":
        new_raw_pass = ''
        for index in range(len(initial_string)):
            if index % 2 == 1:
                new_raw_pass += initial_string[index]
        initial_string = new_raw_pass
        print(initial_string)

    elif action == 'Cut':
        index = int(command_list[1])
        length = int(command_list[2])
        end_index = index + length

        cutted_string = initial_string[index: end_index]
        initial_string = initial_string.replace(cutted_string, '', 1)
        print(initial_string)

    elif action == 'Substitute':
        substring = command_list[1]
        substitute = command_list[2]
        if substring in initial_string:
            initial_string = initial_string.replace(substring, substitute)
            print(initial_string)
        else:
            print("Nothing to replace!")
