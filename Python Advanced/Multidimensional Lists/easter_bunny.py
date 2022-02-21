size = int(input())

field = []
bunny_position = None
total_eggs_from_positions = {'right': 0, 'left': 0, 'up': 0, 'down': 0}
moves_by_directions = {'up': [], 'down': [], 'left': [], 'right': []}

for row in range(size):
    current_row = input().split()
    field.append(current_row)
    if 'B' in current_row:
        bunny_position = (row, current_row.index('B'))

# right moving:
for column in range(bunny_position[1] + 1, size):
    if field[bunny_position[0]][column] != 'X':
        total_eggs_from_positions['right'] += int(field[bunny_position[0]][column])
        moves_by_directions['right'].append([bunny_position[0], column])
    else:
        break

# left moving:
for column in range(bunny_position[1] - 1, -1, -1):
    if field[bunny_position[0]][column] != 'X':
        total_eggs_from_positions['left'] += int(field[bunny_position[0]][column])
        moves_by_directions['left'].append([bunny_position[0], column])
    else:
        break

# up moving:
for row in range(bunny_position[0] - 1, -1, -1):
    if field[row][bunny_position[1]] != 'X':
        total_eggs_from_positions['up'] += int(field[row][bunny_position[1]])
        moves_by_directions['up'].append([row, bunny_position[1]])
    else:
        break

# down moving:
for row in range(bunny_position[0] + 1, size):
    if field[row][bunny_position[1]] != 'X':
        total_eggs_from_positions['down'] += int(field[row][bunny_position[1]])
        moves_by_directions['down'].append([row, bunny_position[1]])
    else:
        break

best_direction = max(total_eggs_from_positions, key=total_eggs_from_positions.get)
print(best_direction)

for position in moves_by_directions[best_direction]:
    print(position)

print(total_eggs_from_positions[best_direction])
