from collections import deque

starting_quantity = int(input())

people = deque()

while True:
    command = input()
    if command == 'Start':
        break

    people.append(command)

while True:
    command = input()
    if command == 'End':
        break

    if command.isdigit():
        if int(command) <= starting_quantity:
            starting_quantity -= int(command)
            print(f'{people.popleft()} got water')
        else:
            print(f'{people.popleft()} must wait')

    else:
        starting_quantity += int(command.split()[1])

print(f'{starting_quantity} liters left')
