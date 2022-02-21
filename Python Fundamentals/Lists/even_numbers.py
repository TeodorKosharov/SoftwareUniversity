# string = input().split(', ')
# integer_list = list(map(int, string))
#
# indicates_list = []
# index = 0
# for number in integer_list:
#     if number % 2 == 0:
#         indicates_list.append(index)
#     index += 1
#
# print(indicates_list)

sequence = [int(x) for x in input().split(', ')]
even_indices = []

for index in range(len(sequence)):
    if sequence[index] % 2 == 0:
        even_indices.append(index)

print(even_indices)
