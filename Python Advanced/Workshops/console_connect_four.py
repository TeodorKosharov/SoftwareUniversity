def display_field(field_matrix):
    for r in field_matrix:
        print(f'[ {", ".join(r)} ]')


def position_marking(given_col, field_matrix, matrix_rows_size):
    try:
        for row in range(matrix_rows_size - 1, -1, -1):
            if field_matrix[row][given_col - 1] == '0':
                return row
        else:
            return 'Out of empty columns! Please enter a new column!'

    except IndexError:
        return 'Please enter a valid column!'


def is_inside(r, c, row_size, col_size=7):
    return 0 <= r < row_size and 0 <= c < col_size


def winning_position_checker(check_row, check_col, field_matrix, matrix_size, check_player):
    # checking vertcal positions:
    vertical_counter = 1

    # left positions:
    for column in range(check_col - 1, -1, -1):
        if field_matrix[check_row][column] == check_player:
            vertical_counter += 1
        else:
            break

    # right positions:
    for column in range(check_col + 1, matrix_size, + 1):
        if field_matrix[check_row][column] == check_player:
            vertical_counter += 1
        else:
            break

    if vertical_counter >= 4:
        return True

    # checking horizontal positions:
    horizontal_counter = 1

    # upward positions:
    for row in range(check_row - 1, -1, -1):
        if field_matrix[row][check_col] == check_player:
            horizontal_counter += 1
        else:
            break

    # downward positions:
    for row in range(check_row + 1, matrix_size, + 1):
        if field_matrix[row][check_col] == check_player:
            horizontal_counter += 1
        else:
            break

    if horizontal_counter >= 4:
        return True

    # checking first diagonal /
    first_diagonal_counter = 1

    # up
    col_index = check_col
    for row in range(check_row - 1, -1, -1):
        if is_inside(row, col_index + 1, matrix_size) and field_matrix[row][col_index + 1] == check_player:
            first_diagonal_counter += 1
            col_index += 1
        else:
            break

    # down
    col_index = check_col
    for row in range(check_row + 1, matrix_size, + 1):
        if is_inside(row, col_index - 1, matrix_size) and field_matrix[row][col_index - 1] == check_player:
            first_diagonal_counter += 1
            col_index -= 1
        else:
            break

    if first_diagonal_counter >= 4:
        return True

    # checking second diagonal \
    second_diagonal_counter = 1

    # up
    col_index = check_col
    for row in range(check_row - 1, -1, -1):
        if is_inside(row, col_index - 1, matrix_size) and field_matrix[row][col_index - 1] == check_player:
            second_diagonal_counter += 1
            col_index -= 1
        else:
            break

    # down
    col_index = check_col
    for row in range(check_row + 1, matrix_size, + 1):
        if is_inside(row, col_index + 1, matrix_size) and field_matrix[row][col_index + 1] == check_player:
            second_diagonal_counter += 1
            col_index += 1
        else:
            break

    if second_diagonal_counter >= 4:
        return True

    return False


field = []
rows = int(input())
for i in range(rows):
    field.append(['0' for x in range(7)])

display_field(field)

while True:
    print('Player 1, please choose a column.')

    while True:
        col = int(input())
        result = position_marking(col, field, rows)
        if type(result) == int:
            field[result][col - 1] = '1'

            if winning_position_checker(result, col - 1, field, rows, '1'):
                print('The winner is player 1')
                display_field(field)
                exit(0)

            display_field(field)
            break

        # if the return value is not int, we need to print the returned string and try with different column
        print(result)

    print('Player 2, please choose a column.')

    while True:
        col = int(input())
        result = position_marking(col, field, rows)
        if type(result) == int:
            field[result][col - 1] = '2'

            if winning_position_checker(result, col - 1, field, rows, '2'):
                print('The winner is player 2')
                display_field(field)
                exit(0)

            display_field(field)
            break

        # if the return value is not int, we need to print the returned string and try with different column
        print(result)
