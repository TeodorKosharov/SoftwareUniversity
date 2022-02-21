from sys import maxsize

rows, cols = [int(x) for x in input().split()]
matrix = []

top_sub_matrix = []
maximal_sum = -maxsize

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

# sub_matrix_sample:
# a, a1, a2
# b, b1, b2
# c, c1, c2

for row in range(rows - 2):
    for column in range(cols - 2):
        a = matrix[row][column]
        a1 = matrix[row][column + 1]
        a2 = matrix[row][column + 2]
        first_sub_matrix_row = [a, a1, a2]

        b = matrix[row + 1][column]
        b1 = matrix[row + 1][column + 1]
        b2 = matrix[row + 1][column + 2]
        second_sub_matrix_row = [b, b1, b2]

        c = matrix[row + 2][column]
        c1 = matrix[row + 2][column + 1]
        c2 = matrix[row + 2][column + 2]
        third_sub_matrix_row = [c, c1, c2]

        current_sub_matrix = [first_sub_matrix_row, second_sub_matrix_row, third_sub_matrix_row]
        current_sum = sum([sum(x) for x in current_sub_matrix])

        if current_sum > maximal_sum:
            maximal_sum = current_sum
            top_sub_matrix = current_sub_matrix

print(f'Sum = {maximal_sum}')
print(*top_sub_matrix[0])
print(*top_sub_matrix[1])
print(*top_sub_matrix[2])
