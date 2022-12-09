matrix = []

for row in range(int(input())):
    matrix.extend(input().split(', '))

print([int(x) for x in matrix])
