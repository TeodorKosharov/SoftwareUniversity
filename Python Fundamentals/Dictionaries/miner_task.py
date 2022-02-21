# line = 1
#
# dictionary = {}
#
# while True:
#     command = input()
#     if command == 'stop':
#         break
#
#     if line % 2 == 1:
#         resource = command
#
#     elif line % 2 == 0:
#         quantity = int(command)
#
#     if resource not in dictionary:
#         dictionary[resource] = 0
#     else:
#         dictionary[resource] += quantity
#
#     line += 1
#     quantity = 0
#
# for key in dictionary:
#     value = dictionary[key]
#     print(f'{key} -> {value}')


resources = {}
line = 1
command = input()
while command != 'stop':
    if line % 2 == 1:
        curr_resource = command
        if curr_resource not in resources:
            resources.update({curr_resource: 0})
    else:
        resources[curr_resource] += int(command)

    command = input()
    line += 1

for key, value in resources.items():
    print(f'{key} -> {value}')
