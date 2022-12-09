rols, cols = [int(x) for x in input().split()]

# word model:
# xyx

matrix = []

for row in range(rols):
    matrix.append([])
    for column in range(cols):
        x = chr(97 + row)
        y = chr(97 + row + column)
        result = x + y + x
        matrix[row].append(result)

for row in matrix:
    print(*row)
