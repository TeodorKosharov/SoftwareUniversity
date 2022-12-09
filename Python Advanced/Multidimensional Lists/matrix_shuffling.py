def indices_checker(indices: list, row1, col1, row2, col2):
    if any(True if x < 0 else False for x in indices):
        return False
    if row1 > rows - 1 or row2 > rows - 1:
        return False
    if col1 > cols - 1 or col2 > cols - 1:
        return False
    return True


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    if command[0] == 'swap' and len(command) == 5:
        row1_index, col1_index, row2_index, col2_index = [int(x) for x in command[1:]]
        all_indices = [row1_index, col1_index, row2_index, col2_index]

        if indices_checker(all_indices, row1_index, col1_index, row2_index, col2_index):
            first_value = matrix[row1_index][col1_index]
            second_value = matrix[row2_index][col2_index]
            matrix[row1_index][col1_index], matrix[row2_index][col2_index] = second_value, first_value

            for row in matrix:
                print(*row)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
