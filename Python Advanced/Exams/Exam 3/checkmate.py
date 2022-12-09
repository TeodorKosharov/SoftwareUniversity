def is_inside(check_row, check_col, size=8):
    return 0 <= check_row < size and 0 <= check_col < size


board = []

queens_positions = []
capturing_queens = []

for row in range(8):
    current_line = input().split()
    board.append(current_line)

    for column in range(len(current_line)):
        if current_line[column] == 'Q':
            queens_positions.append((row, column))

for queen in queens_positions:
    queen_row, queen_col = queen

    # upward:
    for row in range(queen_row - 1, -1, -1):
        if board[row][queen_col] == 'K':
            capturing_queens.append(queen)
        elif board[row][queen_col] == 'Q':
            break

    # downward:
    for row in range(queen_row + 1, 8):
        if board[row][queen_col] == 'K':
            capturing_queens.append(queen)
        elif board[row][queen_col] == 'Q':
            break

    # left:
    for column in range(queen_col - 1, -1, -1):
        if board[queen_row][column] == 'K':
            capturing_queens.append(queen)
        elif board[queen_row][column] == 'Q':
            break

    # right:
    for column in range(queen_col + 1, 8):
        if board[queen_row][column] == 'K':
            capturing_queens.append(queen)
        elif board[queen_row][column] == 'Q':
            break

    # up-right diagonal:
    for value in range(1, 8):
        if is_inside(queen_row - value, queen_col + value):
            if board[queen_row - value][queen_col + value] == 'K':
                capturing_queens.append(queen)
            elif board[queen_row - value][queen_col + value] == 'Q':
                break
        else:
            break

    # up-left diagonal:
    for value in range(1, 8):
        if is_inside(queen_row - value, queen_col - value):
            if board[queen_row - value][queen_col - value] == 'K':
                capturing_queens.append(queen)
            elif board[queen_row - value][queen_col - value] == 'Q':
                break
        else:
            break

    # down-right diagonal:
    for value in range(1, 8):
        if is_inside(queen_row + value, queen_col + value):
            if board[queen_row + value][queen_col + value] == 'K':
                capturing_queens.append(queen)
            elif board[queen_row + value][queen_col + value] == 'Q':
                break
        else:
            break

    # down-left diagonal:
    for value in range(1, 8):
        if is_inside(queen_row + value, queen_col - value):
            if board[queen_row + value][queen_col - value] == 'K':
                capturing_queens.append(queen)
            elif board[queen_row + value][queen_col - value] == 'Q':
                break
        else:
            break

if capturing_queens:
    for queen in capturing_queens:
        print(list(queen))
else:
    print('The king is safe!')
