def get_square(check_row, check_col):
    row = 8 - check_row

    if check_col == 0:
        return f'a{row}'
    elif check_col == 1:
        return f'b{row}'
    elif check_col == 2:
        return f'c{row}'
    elif check_col == 3:
        return f'd{row}'
    elif check_col == 4:
        return f'e{row}'
    elif check_col == 5:
        return f'f{row}'
    elif check_col == 6:
        return f'g{row}'
    elif check_col == 7:
        return f'h{row}'


board = []

white_position = None
black_position = None

for i in range(8):
    current_row = input().split()
    board.append(current_row)

    for col in range(len(current_row)):
        if 'w' in current_row[col]:
            white_position = [i, col]

        if 'b' in current_row[col]:
            black_position = [i, col]

player = 1

while True:
    player_turn = white_position if player % 2 != 0 else black_position
    player += 1

    if player_turn == white_position:
        white_position[0] -= 1

        if white_position[0] == 0:
            print(f'Game over! White pawn is promoted to a queen at {get_square(white_position[0], white_position[1])}.')
            exit(0)

        # left diagonal:
        if white_position[0] == black_position[0] and white_position[1] - 1 == black_position[1]:
            print(f'Game over! White win, capture on {get_square(black_position[0], black_position[1])}.')
            exit(0)

        # right diagonal:
        elif white_position[0] == black_position[0] and white_position[1] + 1 == black_position[1]:
            print(f'Game over! White win, capture on {get_square(black_position[0], black_position[1])}.')
            exit(0)

    elif player_turn == black_position:
        black_position[0] += 1

        if black_position[0] == 7:
            print(f'Game over! Black pawn is promoted to a queen at {get_square(black_position[0], black_position[1])}.')
            exit(0)

        # left diagonal:
        if black_position[0] == white_position[0] and black_position[1] - 1 == white_position[1]:
            print(f'Game over! Black win, capture on {get_square(white_position[0], white_position[1])}.')
            exit(0)

        # right diagonal:
        elif black_position[0] == white_position[0] and black_position[1] + 1 == white_position[1]:
            print(f'Game over! Black win, capture on {get_square(white_position[0], white_position[1])}.')
            exit(0)

