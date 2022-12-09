def is_inside(r, c, row_size, col_size):
    return 0 <= r < row_size and 0 <= c < col_size and r >= 0 and c >= 0


def field_printing(matrix):
    for x in matrix:
        print(*x, sep='')


def win_state(r, c, matrix):
    field_printing(matrix)
    print(f"won: {r} {c}")


def dead_state(r, c, matrix):
    field_printing(matrix)
    print(f"dead: {r} {c}")


def get_next_position(player_row, player_col, comm):
    if comm == 'L':
        return player_row, player_col - 1
    elif comm == 'R':
        return player_row, player_col + 1
    elif command == 'U':
        return player_row - 1, player_col
    elif comm == 'D':
        return player_row + 1, player_col


def is_player_there(r, c, matrix):
    if matrix[r][c] == 'P':
        return True
    return False


rows, cols = map(int, input().split())

field = []
bunnies_coords = set()
player_coords = None
is_player_dead = False
is_player_winner = False

for row in range(rows):
    current_row = list(input())
    field.append(current_row)

    for el in range(len(current_row)):
        if current_row[el] == 'P':
            player_coords = (row, el)

        if current_row[el] == 'B':
            bunnies_coords.add((row, el))

commands = input()

for command in commands:
    next_position = get_next_position(player_coords[0], player_coords[1], command)
    field[player_coords[0]][player_coords[1]] = '.'  # removing player last position

    if not is_inside(next_position[0], next_position[1], rows, cols):  # player wins
        is_player_winner = True
    else:
        player_coords = next_position[0], next_position[1]
        if field[player_coords[0]][player_coords[1]] == 'B':  # if player steps on bunny
            is_player_dead = True
        else:
            field[player_coords[0]][player_coords[1]] = 'P'  # setting the new position of the player

    new_bunny_coords = set()
    for bunny in bunnies_coords:
        spawn_up = bunny[0] - 1, bunny[1]
        spawn_down = bunny[0] + 1, bunny[1]
        spawn_left = bunny[0], bunny[1] - 1
        spawn_right = bunny[0], bunny[1] + 1

        if is_inside(spawn_up[0], spawn_up[1], rows, cols):
            if is_player_there(spawn_up[0], spawn_up[1], field):
                is_player_dead = True
            field[spawn_up[0]][spawn_up[1]] = 'B'
            new_bunny_coords.add((spawn_up[0], spawn_up[1]))

        if is_inside(spawn_down[0], spawn_down[1], rows, cols):
            if is_player_there(spawn_down[0], spawn_down[1], field):
                is_player_dead = True
            field[spawn_down[0]][spawn_down[1]] = 'B'
            new_bunny_coords.add((spawn_down[0], spawn_down[1]))

        if is_inside(spawn_left[0], spawn_left[1], rows, cols):
            if is_player_there(spawn_left[0], spawn_left[1], field):
                is_player_dead = True
            field[spawn_left[0]][spawn_left[1]] = 'B'
            new_bunny_coords.add((spawn_left[0], spawn_left[1]))

        if is_inside(spawn_right[0], spawn_right[1], rows, cols):
            if is_player_there(spawn_right[0], spawn_right[1], field):
                is_player_dead = True
            field[spawn_right[0]][spawn_right[1]] = 'B'
            new_bunny_coords.add((spawn_right[0], spawn_right[1]))

    bunnies_coords = bunnies_coords.union(new_bunny_coords)

    if is_player_winner:
        win_state(player_coords[0], player_coords[1], field)
        exit(0)

    if is_player_dead:
        dead_state(player_coords[0], player_coords[1], field)
        exit(0)
