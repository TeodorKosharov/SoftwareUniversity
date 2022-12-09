def is_inside(check_row, check_col, matrix_size):
    return 0 <= check_row < matrix_size and 0 <= check_col < matrix_size


size = int(input())
bombs = int(input())

field = []

for row in range(size):
    field.append([])
    for col in range(size):
        field[row].append(0)

for i in range(bombs):
    bomb_position = input()
    bomb_row, bomb_col = eval(bomb_position)
    field[bomb_row][bomb_col] = '*'

    # up:
    if is_inside(bomb_row - 1, bomb_col, size) and type(field[bomb_row - 1][bomb_col]) == int:
        field[bomb_row - 1][bomb_col] += 1

    # down:
    if is_inside(bomb_row + 1, bomb_col, size) and type(field[bomb_row + 1][bomb_col]) == int:
        field[bomb_row + 1][bomb_col] += 1

    # left:
    if is_inside(bomb_row, bomb_col - 1, size) and type(field[bomb_row][bomb_col - 1]) == int:
        field[bomb_row][bomb_col - 1] += 1

    # right:
    if is_inside(bomb_row, bomb_col + 1, size) and type(field[bomb_row][bomb_col + 1]) == int:
        field[bomb_row][bomb_col + 1] += 1

    # up-right:
    if is_inside(bomb_row - 1, bomb_col + 1, size) and type(field[bomb_row - 1][bomb_col + 1]) == int:
        field[bomb_row - 1][bomb_col + 1] += 1

    # up-left:
    if is_inside(bomb_row - 1, bomb_col - 1, size) and type(field[bomb_row - 1][bomb_col - 1]) == int:
        field[bomb_row - 1][bomb_col - 1] += 1

    # down-right:
    if is_inside(bomb_row + 1, bomb_col + 1, size) and type(field[bomb_row + 1][bomb_col + 1]) == int:
        field[bomb_row + 1][bomb_col + 1] += 1

    # down-left:
    if is_inside(bomb_row + 1, bomb_col - 1, size) and type(field[bomb_row + 1][bomb_col - 1]) == int:
        field[bomb_row + 1][bomb_col - 1] += 1

for field_row in field:
    print(*field_row)
