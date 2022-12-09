def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


def neighbourhood_printing(matrix):
    for row in matrix:
        print(*row)


presents = int(input())
size = int(input())

neighbourhood = []
nice_kids = 0
santa_position = None
flag = False

for row in range(size):
    current_row = input().split()
    neighbourhood.append(current_row)

    if 'S' in current_row:
        santa_position = (row, current_row.index('S'))
    if 'V' in current_row:
        nice_kids += current_row.count('V')

nice_kids_copy = nice_kids

while True:
    command = input()
    if command == "Christmas morning":
        break

    elif command == 'up':
        if is_inside(santa_position[0] - 1, santa_position[1], size):
            neighbourhood[santa_position[0]][santa_position[1]] = '-'
            santa_position = (santa_position[0] - 1, santa_position[1])

    elif command == 'down':
        if is_inside(santa_position[0] + 1, santa_position[1], size):
            neighbourhood[santa_position[0]][santa_position[1]] = '-'
            santa_position = (santa_position[0] + 1, santa_position[1])

    elif command == 'left':
        if is_inside(santa_position[0], santa_position[1] - 1, size):
            neighbourhood[santa_position[0]][santa_position[1]] = '-'
            santa_position = (santa_position[0], santa_position[1] - 1)

    elif command == 'right':
        if is_inside(santa_position[0], santa_position[1] + 1, size):
            neighbourhood[santa_position[0]][santa_position[1]] = '-'
            santa_position = (santa_position[0], santa_position[1] + 1)

    if neighbourhood[santa_position[0]][santa_position[1]] == 'V':
        presents -= 1
        nice_kids -= 1
        neighbourhood[santa_position[0]][santa_position[1]] = 'S'
        if presents == 0:
            break

    elif neighbourhood[santa_position[0]][santa_position[1]] == 'X':
        neighbourhood[santa_position[0]][santa_position[1]] = 'S'

    elif neighbourhood[santa_position[0]][santa_position[1]] == 'C':
        neighbourhood[santa_position[0]][santa_position[1]] = 'S'
        side_positions = {}

        up_position = (santa_position[0] - 1, santa_position[1])
        down_position = (santa_position[0] + 1, santa_position[1])
        left_position = (santa_position[0], santa_position[1] - 1)
        right_position = (santa_position[0], santa_position[1] + 1)

        side_positions[up_position] = neighbourhood[up_position[0]][up_position[1]]
        side_positions[down_position] = neighbourhood[down_position[0]][down_position[1]]
        side_positions[left_position] = neighbourhood[left_position[0]][left_position[1]]
        side_positions[right_position] = neighbourhood[right_position[0]][right_position[1]]

        for position, symbol in side_positions.items():
            if symbol == 'V':
                presents -= 1
                nice_kids -= 1
            elif symbol == 'X':
                presents -= 1
            neighbourhood[position[0]][position[1]] = '-'
            if presents == 0:
                flag = True
                break
    if flag:
        break

if nice_kids == 0:
    neighbourhood_printing(neighbourhood)
    print(f"Good job, Santa! {nice_kids_copy} happy nice kid/s.")
elif presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")
    neighbourhood_printing(neighbourhood)
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    neighbourhood_printing(neighbourhood)
    print(f"No presents for {nice_kids} nice kid/s.")
