# dictionary = {}
#
# while True:
#     contact = input()
#
#     if contact.isdigit():
#         break
#
#     contact_list = contact.split('-')
#     name = contact_list[0]
#     number = contact_list[1]
#     dictionary[name] = number
#
# n = int(contact)
#
# for i in range(n):
#     check_name = input()
#
#     if check_name in dictionary:
#         number = dictionary[check_name]
#         print(f'{check_name} -> {number}')
#     else:
#         print(f"Contact {check_name} does not exist.")


users = {}

while True:
    user_data = input().split('-')
    if user_data[0].isdigit():
        break
    users.update({user_data[0]: user_data[1]})

for _ in range(int(user_data[0])):
    name = input()
    if name not in users:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {users[name]}")
