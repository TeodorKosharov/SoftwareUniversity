encrypted_message = input()

while True:
    inp = input()
    if inp == 'Decode':
        break

    inp = inp.split('|')
    command = inp[0]

    if command == 'Move':
        number_of_letters = int(inp[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif command == 'Insert':
        index = int(inp[1])
        value = inp[2]
        left_half = encrypted_message[:index]
        righ_half = encrypted_message[index:]
        encrypted_message = left_half + value + righ_half

    elif command == 'ChangeAll':
        substring = inp[1]
        replacement = inp[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")

### Втори начин:
# encrypted_message = input()
#
# while True:
#     command = input()
#     if command == 'Decode':
#         break
#
#     command_list = command.split('|')
#     action = command_list[0]
#     encrypted_message = [char for char in encrypted_message]
#
#     if action == 'Move':
#         number_of_letters = int(command_list[1])
#         cutted_part = encrypted_message[:number_of_letters]
#         rest_part = encrypted_message[number_of_letters:]
#         encrypted_message = rest_part + cutted_part
#
#     elif action == 'Insert':
#         index = int(command_list[1])
#         value = command_list[2]
#         encrypted_message.insert(index, value)
#         encrypted_message_copy = encrypted_message.copy()
#         encrypted_message = ''
#         for char in encrypted_message_copy:
#             encrypted_message += char
#
#     elif action == 'ChangeAll':
#         substring = command_list[1]
#         replacement = command_list[2]
#         encrypted_message_copy = encrypted_message.copy()
#         encrypted_message = ''
#         for char in encrypted_message_copy:
#             encrypted_message += char
#         encrypted_message = encrypted_message.replace(substring, replacement)
#
# print(f"The decrypted message is: {''.join(encrypted_message)}")
