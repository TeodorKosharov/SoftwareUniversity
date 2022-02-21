size = int(input())

matrix = []
for row in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()

    if command[0] == 'Add':
        row, col = int(command[1]), int(command[2])
        if 0 <= row < size and 0 <= col < size:
            matrix[row][col] += int(command[3])
        else:
            print("Invalid coordinates")

    elif command[0] == 'Subtract':
        row, col = int(command[1]), int(command[2])
        if 0 <= row < size and 0 <= col < size:
            matrix[row][col] -= int(command[3])
        else:
            print("Invalid coordinates")
    else:
        break

for row in matrix:
    print(*row)
