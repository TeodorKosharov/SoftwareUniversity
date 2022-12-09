n = int(input())
commands = input().split()

matrix = []
position = None
total_coal = 0

for row in range(n):
    current_row = input().split()
    if 's' in current_row:
        position = [row, current_row.index('s')]
    if 'c' in current_row:
        total_coal += len([x for x in current_row if x == 'c'])
    matrix.append(current_row)

# miner position model:  [row, column]

for command in commands:
    if command == 'right':
        if position[1] + 1 <= n - 1:
            position[1] += 1

    elif command == 'left':
        if position[1] - 1 >= 0:
            position[1] -= 1

    elif command == 'up':
        if position[0] - 1 >= 0:
            position[0] -= 1

    elif command == 'down':
        if position[0] + 1 <= n - 1:
            position[0] += 1

    if matrix[position[0]][position[1]] == 'e':
        print(f"Game over! ({position[0]}, {position[1]})")
        exit()

    elif matrix[position[0]][position[1]] == 'c':
        total_coal -= 1

    matrix[position[0]][position[1]] = '*'

if total_coal == 0:
    print(f"You collected all coal! ({position[0]}, {position[1]})")
else:
    print(f"{total_coal} pieces of coal left. ({position[0]}, {position[1]})")
