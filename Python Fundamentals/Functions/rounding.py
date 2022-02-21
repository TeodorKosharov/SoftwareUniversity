string = input().split()

numbers_list = list(map(float, string))

result_list = []

for element in numbers_list:
    result_list.append(round(element))

print(result_list)
