rows, cols = map(int, input().split())

equal_squares = 0
matrix = []

for row in range(rows):
    matrix.append([x for x in input().split()])

for row in range(rows - 1):
    for column in range(cols - 1):
        first_element = matrix[row][column]
        second_element = matrix[row][column + 1]
        third_element = matrix[row + 1][column]
        fourth_element = matrix[row + 1][column + 1]

        if first_element == second_element == third_element == fourth_element:
            equal_squares += 1

print(equal_squares)
