def is_inside(check_row, check_col, matrix_size):
    return 0 <= check_row < matrix_size and 0 <= check_col < matrix_size


def get_next_position(snake_r, snake_c, comm):
    if comm == 'up':
        return snake_r - 1, snake_c
    elif comm == 'down':
        return snake_r + 1, snake_c
    elif comm == 'left':
        return snake_r, snake_c - 1
    elif comm == 'right':
        return snake_r, snake_c + 1


size = int(input())

territory = []
burrow_positions = []
collected_food = 0
snake_position = None
is_game_over = False

for row in range(size):
    current_row = list(input())
    territory.append(current_row)

    if 'S' in current_row:
        snake_position = (row, current_row.index('S'))
    if 'B' in current_row:
        burrow_positions.append((row, current_row.index('B')))

while collected_food < 10:
    command = input()
    current_snake_row, current_snake_col = snake_position
    next_snake_row, next_snake_col = get_next_position(snake_position[0], snake_position[1], command)

    if is_inside(next_snake_row, next_snake_col, size):
        if territory[next_snake_row][next_snake_col] == '*':
            collected_food += 1

        elif territory[next_snake_row][next_snake_col] == 'B':
            territory[next_snake_row][next_snake_col] = '.'
            burrow_positions.remove((next_snake_row, next_snake_col))
            remaining_burrow = burrow_positions[0]
            next_snake_row, next_snake_col = remaining_burrow

        territory[current_snake_row][current_snake_col] = '.'
        snake_position = next_snake_row, next_snake_col
        territory[next_snake_row][next_snake_col] = 'S'
    else:
        territory[current_snake_row][current_snake_col] = '.'
        is_game_over = True
        break

if is_game_over:
    print('Game over!')
else:
    print('You won! You fed the snake.')

print(f'Food eaten: {collected_food}')

for row in territory:
    print(''.join(row))
