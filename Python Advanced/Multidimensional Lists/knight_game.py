def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = []
removed_knights = 0
power = 0
best_power = 0
powerful_knight_coords = (0, 0)

for _ in range(size):
    matrix.append(list(input()))

while True:
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                power = 0

                # up-left move
                if is_inside(row - 2, col - 1, size):
                    if matrix[row - 2][col - 1] == 'K':
                        power += 1

                # up-right move
                if is_inside(row - 2, col + 1, size):
                    if matrix[row - 2][col + 1] == 'K':
                        power += 1

                # right-top move
                if is_inside(row - 1, col + 2, size):
                    if matrix[row - 1][col + 2] == 'K':
                        power += 1

                # right-bottom move
                if is_inside(row + 1, col + 2, size):
                    if matrix[row + 1][col + 2] == 'K':
                        power += 1

                # bottom-right move
                if is_inside(row + 2, col + 1, size):
                    if matrix[row + 2][col + 1] == 'K':
                        power += 1

                # bottom-left move
                if is_inside(row + 2, col - 1, size):
                    if matrix[row + 2][col - 1] == 'K':
                        power += 1

                # left-bottom move
                if is_inside(row + 1, col - 2, size):
                    if matrix[row + 1][col - 2] == 'K':
                        power += 1

                # left-top move
                if is_inside(row - 1, col - 2, size):
                    if matrix[row - 1][col - 2] == 'K':
                        power += 1

                if power > best_power:
                    best_power = power
                    powerful_knight_coords = (row, col)

    if powerful_knight_coords[0] == 0 and powerful_knight_coords[1] == 0:
        break
    else:
        matrix[powerful_knight_coords[0]][powerful_knight_coords[1]] = 0
        removed_knights += 1

    best_power = 0
    powerful_knight_coords = (0, 0)

print(removed_knights)
