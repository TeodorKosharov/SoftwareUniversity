from termcolor import colored


def game():

    def get_sign_color(color_option):

        if color_option == 1:
            return 'green'
        elif color_option == 2:
            return 'yellow'
        elif color_option == 3:
            return 'blue'
        elif color_option == 4:
            return 'magenta'
        elif color_option == 5:
            return 'cyan'
        elif color_option <= 0 or color_option > 5:
            print('Please choose valid color! ', end='')
            new_choice = int(input())
            return get_sign_color(new_choice)

    def color_determination():
        global first_player_sign_color
        global second_player_sign_color

        print('Color options:')
        print('1) Green')
        print('2) Yellow')
        print('3) Blue')
        print('4) Magenta')
        print('5) Cyan')

        print(f'{first_player}, please choose sign color from the options above: ', end='')
        choice = int(input())
        first_player_sign_color = get_sign_color(choice)

        print(f'{second_player}, please choose sign color from the options above: ', end='')
        choice = int(input())
        second_player_sign_color = get_sign_color(choice)

        while second_player_sign_color == first_player_sign_color:
            choice = int(input('This color is already taken. Please choose another option! '))
            second_player_sign_color = get_sign_color(choice)

    def get_position(value):
        if value == 1:
            return 0, 0
        elif value == 2:
            return 0, 1
        elif value == 3:
            return 0, 2
        elif value == 4:
            return 1, 0
        elif value == 5:
            return 1, 1
        elif value == 6:
            return 1, 2
        elif value == 7:
            return 2, 0
        elif value == 8:
            return 2, 1
        elif value == 9:
            return 2, 2

    def is_position_free(check_row, check_col, matrix):
        if 'X' not in matrix[check_row][check_col] and 'O' not in matrix[check_row][check_col]:
            return True
        return False

    def display_board(matrix):
        for r in matrix:
            print(*r)

    def state():
        global position
        global first_player_sign_color
        global second_player_sign_color
        global free_positions

        while position <= 0 or position > 9:
            position = int(input('Please enter a valid position!'))

        row, col = get_position(position)

        if is_position_free(row, col, board):
            board[row][col] = board[row][col][:3] + colored(first_player_sign, first_player_sign_color) + board[row][col][4:]
            first_player_sign_color, second_player_sign_color = second_player_sign_color, first_player_sign_color
            free_positions -= 1
        else:
            print('The entered position is not free!')
            position = int(input('Please enter a free position! '))
            state()

    def winner_check(matrix, check_sign, player):
        first_row = all([check_sign in x for x in matrix[0]])
        second_row = all([check_sign in x for x in matrix[1]])
        third_row = all([check_sign in x for x in matrix[2]])
        first_column = all([check_sign in x for x in [matrix[0][0], matrix[1][0], matrix[2][0]]])
        second_column = all([check_sign in x for x in [matrix[0][1], matrix[1][1], matrix[2][1]]])
        third_column = all([check_sign in x for x in [matrix[0][2], matrix[1][2], matrix[2][2]]])
        first_diagonal = all([check_sign in x for x in [matrix[0][2], matrix[1][1], matrix[2][0]]])
        second_diagonal = all([check_sign in x for x in [matrix[0][0], matrix[1][1], matrix[2][2]]])

        if any([first_row,
                second_row,
                third_row,
                first_column,
                second_column,
                third_column,
                first_diagonal,
                second_diagonal]):
            return f'{player} won!'
        return False

    def continuation_of_the_game():
        answer = input('Do you want to start new game? [Yes/No] ')
        if answer == 'Yes':
            game()
        else:
            print('Goodbye!')
            exit(0)

    global free_positions
    free_positions = 9

    board = [
        ['|  1 ', '|  2 ', '|  3  |'],
        ['|  4 ', '|  5 ', '|  6  |'],
        ['|  7 ', '|  8 ', '|  9  |']
    ]

    first_player = input('Player one name: ')
    second_player = input('Player two name: ')
    first_player_sign = input(f'{first_player}, would you like to play with "X" or "O"? ')

    while first_player_sign != 'X' and first_player_sign != 'O':
        first_player_sign = input('Please choose a valid sign! ')

    if first_player_sign == 'X':
        second_player_sign = 'O'
    else:
        second_player_sign = 'X'

    color_determination()

    print('This is the numeration of the board:')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')
    print(f'{first_player} starts first!')

    while True:
        global position

        position = int(input(f'{first_player} [{colored(first_player_sign, first_player_sign_color)}] choose a free and valid position: '))
        state()
        if winner_check(board, first_player_sign, first_player):
            display_board(board)
            print(winner_check(board, first_player_sign, first_player))
            print(colored('Game ended!', 'red'))
            continuation_of_the_game()

        if free_positions == 0:
            display_board(board)
            print(colored('Draw! No winner!', 'red'))
            continuation_of_the_game()

        first_player, second_player = second_player, first_player
        first_player_sign, second_player_sign = second_player_sign, first_player_sign
        display_board(board)


game()
