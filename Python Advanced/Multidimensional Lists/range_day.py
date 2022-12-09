def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


def matrix_printring(matrix: list):
    for row in matrix:
        print(row)


size = 5

shooting_area = []
my_position = None
total_targets = 0
hit_targets = []

for row in range(size):
    current_row = input().split()
    shooting_area.append(current_row)

    if 'A' in current_row:
        my_position = (row, current_row.index('A'))
    if 'x' in current_row:
        total_targets += current_row.count('x')

count_targets = total_targets

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        direction = command[1]
        steps = int(command[2])

        if direction == 'right':
            if is_inside(my_position[0], my_position[1] + steps, size) and \
                    shooting_area[my_position[0]][my_position[1] + steps] == '.':
                my_position = (my_position[0], my_position[1] + steps)

        elif direction == 'left':
            if is_inside(my_position[0], my_position[1] - steps, size) and \
                    shooting_area[my_position[0]][my_position[1] - steps] == '.':
                my_position = (my_position[0], my_position[1] - steps)

        elif direction == 'up':
            if is_inside(my_position[0] - steps, my_position[1], size) and \
                    shooting_area[my_position[0] - steps][my_position[1]] == '.':
                my_position = (my_position[0] - steps, my_position[1])

        elif direction == 'down':
            if is_inside(my_position[0] + steps, my_position[1], size) and \
                    shooting_area[my_position[0] + steps][my_position[1]] == '.':
                my_position = (my_position[0] + steps, my_position[1])

    elif command[0] == 'shoot':
        direction = command[1]

        if direction == 'right':
            for column in range(my_position[1] + 1, size):
                if shooting_area[my_position[0]][column] == 'x':
                    total_targets -= 1
                    shooting_area[my_position[0]][column] = '.'
                    hit_targets.append([my_position[0], column])
                    break

        elif direction == 'left':
            for column in range(my_position[1] - 1, -1, -1):
                if shooting_area[my_position[0]][column] == 'x':
                    total_targets -= 1
                    shooting_area[my_position[0]][column] = '.'
                    hit_targets.append([my_position[0], column])
                    break

        elif direction == 'up':
            for row in range(my_position[0] - 1, -1, -1):
                if shooting_area[row][my_position[1]] == 'x':
                    total_targets -= 1
                    shooting_area[row][my_position[1]] = '.'
                    hit_targets.append([row, my_position[1]])
                    break

        elif direction == 'down':
            for row in range(my_position[0] + 1, size):
                if shooting_area[row][my_position[1]] == 'x':
                    total_targets -= 1
                    shooting_area[row][my_position[1]] = '.'
                    hit_targets.append([row, my_position[1]])
                    break

        if total_targets == 0:
            print(f"Training completed! All {count_targets} targets hit.")
            matrix_printring(hit_targets)
            exit()

print(f"Training not completed! {total_targets} targets left.")
matrix_printring(hit_targets)
