# string = input()
# beggars = int(input())
#
# numbers = string.split(', ')
# beggars_list = [0] * beggars
#
# counter = 0
#
# for element in numbers:
#
#     beggars_list[counter] += int(element)
#
#     counter += 1
#
#     if counter >= beggars:
#         counter = 0
#
# print(beggars_list)

integers = list(map(int, input().split(', ')))
beggars = int(input())
start_index = 0
result = []

for beggar in range(beggars):
    value = 0
    for current_value in range(start_index, len(integers), beggars):
        value += integers[current_value]

    result.append(value)
    start_index += 1

print(result)
