def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


def territory_printing(matrix: list):
    for row in matrix:
        print(*row)


size = int(input())

territory = []
alice_position = None
tea_bags = 0

for row in range(size):
    current_row = input().split()
    territory.append(current_row)
    if 'A' in current_row:
        alice_position = (row, current_row.index('A'))

while True:
    command = input()
    if command == 'up':
        territory[alice_position[0]][alice_position[1]] = '*'
        alice_position = (alice_position[0] - 1, alice_position[1])

    elif command == 'down':
        territory[alice_position[0]][alice_position[1]] = '*'
        alice_position = (alice_position[0] + 1, alice_position[1])

    elif command == 'left':
        territory[alice_position[0]][alice_position[1]] = '*'
        alice_position = (alice_position[0], alice_position[1] - 1)

    elif command == 'right':
        territory[alice_position[0]][alice_position[1]] = '*'
        alice_position = (alice_position[0], alice_position[1] + 1)

    if is_inside(alice_position[0], alice_position[1], size):
        if territory[alice_position[0]][alice_position[1]].isdigit():
            tea_bags += int(territory[alice_position[0]][alice_position[1]])

            if tea_bags >= 10:
                territory[alice_position[0]][alice_position[1]] = '*'
                print("She did it! She went to the party.")
                territory_printing(territory)
                exit()
        elif territory[alice_position[0]][alice_position[1]] == 'R':
            territory[alice_position[0]][alice_position[1]] = '*'
            break
    else:
        break

print("Alice didn't make it to the tea party.")
territory_printing(territory)
