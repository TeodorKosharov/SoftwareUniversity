# n = int(input())
# usernames = {}
#
# for i in range(n):
#     command = input().split()
#     type = command[0]
#     username = command[1]
#
#     if type == 'register':
#         plate_num = command[2]
#         if username not in usernames:
#             usernames[username] = plate_num
#             print(f"{username} registered {plate_num} successfully")
#         else:
#             print(f"ERROR: already registered with plate number {plate_num}")
#     else:
#         if username not in usernames:
#             print(f"ERROR: user {username} not found")
#         else:
#             usernames.pop(username)
#             print(f"{username} unregistered successfully")
#
# for element in usernames:
#     plate = usernames[element]
#     print(f'{element} => {plate}')


parking_data = {}
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'register':
        if command[1] not in parking_data:
            parking_data.update({command[1]: command[2]})
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[2]}")
    else:
        if command[1] not in parking_data:
            print(f"ERROR: user {command[1]} not found")
        else:
            del parking_data[command[1]]
            print(f"{command[1]} unregistered successfully")

for key, value in parking_data.items():
    print(f"{key} => {value}")
