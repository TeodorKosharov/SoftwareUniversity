rows, cols = map(int, input().split(', '))

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for column in range(cols):
    result = 0
    for row in range(rows):
        result += matrix[row][column]
    print(result)
