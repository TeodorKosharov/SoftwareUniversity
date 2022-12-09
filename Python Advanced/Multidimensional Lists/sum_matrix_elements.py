rows, cols = map(int, input().split(', '))

total_sum = 0
matrix = []
for row in range(rows):
    matrix.append(list(map(int, input().split(', '))))

print(sum(sum([x for x in row]) for row in matrix))
print(matrix)
