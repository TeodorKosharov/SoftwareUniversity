def is_inside(check_row, check_col):
    return 0 <= check_row < size and 0 <= check_col < size


initial_string = input()
size = int(input())

field = []
player_position = None

for row in range(size):
    current_row = list(input())
    field.append(current_row)

    for col_index in range(len(current_row)):
        if current_row[col_index] == 'P':
            player_position = row, col_index

for command in range(int(input())):
    direction = input()
    player_row, player_col = player_position

    if direction == 'up' and is_inside(player_row - 1, player_col):
        next_position = player_row - 1, player_col
    elif direction == 'down' and is_inside(player_row + 1, player_col):
        next_position = player_row + 1, player_col
    elif direction == 'left' and is_inside(player_row, player_col - 1):
        next_position = player_row, player_col - 1
    elif direction == 'right' and is_inside(player_row, player_col + 1):
        next_position = player_row, player_col + 1
    else:
        if initial_string:
            initial_string = initial_string[:-1]
            continue

    field[player_row][player_col] = '-'
    player_position = next_position

    if field[player_position[0]][player_position[1]].isalpha():
        initial_string += field[player_position[0]][player_position[1]]
        field[player_position[0]][player_position[1]] = 'P'

    field[player_position[0]][player_position[1]] = 'P'

print(initial_string)
for row in field:
    print(''.join(row))
