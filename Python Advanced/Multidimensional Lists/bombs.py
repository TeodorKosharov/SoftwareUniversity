def is_inside(row, col):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = input().split()
bombs = []

for bomb in bomb_coordinates:
    bombs.append(list(map(int, bomb.split(','))))

for bomb in bombs:
    bomb_power = matrix[bomb[0]][bomb[1]]
    bomb_row, bomb_col = bomb

    if bomb_power <= 0:
        continue
    else:
        matrix[bomb_row][bomb_col] = 0

    # up coordinates
    if is_inside(bomb_row - 1, bomb_col):
        if matrix[bomb_row - 1][bomb_col] > 0:
            matrix[bomb_row - 1][bomb_col] -= bomb_power

    # down coordinates
    if is_inside(bomb_row + 1, bomb_col):
        if matrix[bomb_row + 1][bomb_col] > 0:
            matrix[bomb_row + 1][bomb_col] -= bomb_power

    # left coordinates
    if is_inside(bomb_row, bomb_col - 1):
        if matrix[bomb_row][bomb_col - 1] > 0:
            matrix[bomb_row][bomb_col - 1] -= bomb_power

    # right coordinates
    if is_inside(bomb_row, bomb_col + 1):
        if matrix[bomb_row][bomb_col + 1] > 0:
            matrix[bomb_row][bomb_col + 1] -= bomb_power

    # top left diagonal
    if is_inside(bomb_row - 1, bomb_col - 1):
        if matrix[bomb_row - 1][bomb_col - 1] > 0:
            matrix[bomb_row - 1][bomb_col - 1] -= bomb_power

    # top right diagonal
    if is_inside(bomb_row - 1, bomb_col + 1):
        if matrix[bomb_row - 1][bomb_col + 1] > 0:
            matrix[bomb_row - 1][bomb_col + 1] -= bomb_power

    # down left diagonal
    if is_inside(bomb_row + 1, bomb_col - 1):
        if matrix[bomb_row + 1][bomb_col - 1] > 0:
            matrix[bomb_row + 1][bomb_col - 1] -= bomb_power

    # down right diagonal
    if is_inside(bomb_row + 1, bomb_col + 1):
        if matrix[bomb_row + 1][bomb_col + 1] > 0:
            matrix[bomb_row + 1][bomb_col + 1] -= bomb_power

alive_cells = 0
sum_of_alive_cells = 0

for row in matrix:
    alives = [x for x in row if x > 0]
    alive_cells += len(alives)
    sum_of_alive_cells += sum(alives)

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_of_alive_cells}')
for i in matrix:
    print(*i)
