def is_inside(check_row, check_col):
    return 0 <= check_row < size and 0 <= check_col < size


def get_next_pos(n_row, n_col):
    if n_row < 0:
        n_row = size - 1
    elif n_row == size:
        n_row = 0

    if n_col < 0:
        n_col = size - 1
    elif n_col == size:
        n_col = 0

    return n_row, n_col


size = int(input())

field = []
player_position = None
player_path = []
coins = 0

for row in range(size):
    current_row = input().split()
    field.append(current_row)

    for col in range(len(current_row)):
        if current_row[col] == 'P':
            player_position = row, col
            player_path.append([row, col])

while coins < 100:
    command = input()
    player_row, player_col = player_position
    next_position = None

    if command == 'up':
        next_position = player_row - 1, player_col
    elif command == 'down':
        next_position = player_row + 1, player_col
    elif command == 'left':
        next_position = player_row, player_col - 1
    elif command == 'right':
        next_position = player_row, player_col + 1

    if is_inside(*next_position):
        if field[next_position[0]][next_position[1]].isdigit():
            coins += int(field[next_position[0]][next_position[1]])
            field[next_position[0]][next_position[1]] = 'P'

        elif field[next_position[0]][next_position[1]] == 'X':
            player_path.append([*next_position])
            coins //= 2
            break

        player_position = next_position[0], next_position[1]
        player_path.append([*next_position])

    else:
        next_row, next_col = get_next_pos(*next_position)

        if field[next_row][next_col].isdigit():
            coins += int(field[next_row][next_col])
            field[next_row][next_col] = 'P'

        elif field[next_row][next_col] == 'X':
            coins //= 2
            player_path.append([next_row, next_col])
            break

        player_path.append([next_row, next_col])
        player_position = next_row, next_col

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for path in player_path:
    print(f"{list(path)}")
