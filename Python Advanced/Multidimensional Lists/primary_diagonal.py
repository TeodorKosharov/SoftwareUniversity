# matrix = []
#
# for row in range(int(input())):
#     matrix.append([int(x) for x in input().split()])
#
# index = 0
# diagonal_sum = 0
# for row in matrix:
#     diagonal_sum += row[index]
#     index += 1
#
# print(diagonal_sum)

# Second variant:

matrix = []
diagonal_sum = 0

for index in range(int(input())):
    diagonal_sum += [int(x) for x in input().split()][index]

print(diagonal_sum)
