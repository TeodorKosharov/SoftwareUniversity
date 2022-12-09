raw_activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        print(f"Your activation key is: {raw_activation_key}")
        break
    command_list = command.split('>>>')
    action = command_list[0]
    if action == 'Contains':
        substring = command_list[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == 'Flip':
        case_command = command_list[1]
        start_index = int(command_list[2])
        end_index = int(command_list[3])
        if case_command == 'Lower':
            raw_activation_key = raw_activation_key[0:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
        elif case_command == 'Upper':
            raw_activation_key = raw_activation_key[0:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
        print(raw_activation_key)

    elif action == 'Slice':
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
