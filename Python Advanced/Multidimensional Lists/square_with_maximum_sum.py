from sys import maxsize

rows, cols = map(int, input().split(', '))

matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

top_sub_matrix = []
top_sub_matrix_sum = -maxsize

for row in range(rows - 1):
    for column in range(cols - 1):
        first_element = matrix[row][column]
        second_element = matrix[row][column + 1]
        third_element = matrix[row + 1][column]
        fourth_element = matrix[row + 1][column + 1]
        sub_matrix = [[first_element, second_element], [third_element, fourth_element]]
        sub_matrix_sum = sum([sum(x) for x in sub_matrix])

        if sub_matrix_sum > top_sub_matrix_sum:
            top_sub_matrix_sum = sub_matrix_sum
            top_sub_matrix = sub_matrix

print(*top_sub_matrix[0])
print(*top_sub_matrix[1])
print(top_sub_matrix_sum)
