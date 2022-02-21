consealed_message = input()

while True:
    command = input()
    if command == 'Reveal':
        print(f"You have a new text message: {consealed_message}")
        exit()
    command_list = command.split(':|:')
    action = command_list[0]
    if action == 'InsertSpace':
        index = int(command_list[1])
        consealed_message = consealed_message[:index] + ' ' + consealed_message[index:]
        print(consealed_message)

    elif action == 'Reverse':
        substring = command_list[1]
        if substring in consealed_message:
            consealed_message = consealed_message.replace(substring, '', 1)
            substring = substring[::-1]
            consealed_message += substring
            print(consealed_message)
        elif substring not in consealed_message:
            print('error')

    elif action == 'ChangeAll':
        substring = command_list[1]
        replacement = command_list[2]
        consealed_message = consealed_message.replace(substring, replacement)
        print(consealed_message)
