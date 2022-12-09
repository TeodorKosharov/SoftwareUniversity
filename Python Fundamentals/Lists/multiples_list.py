# first_value = int(input())
# second_value = int(input())
#
# max_value = first_value * second_value
#
# numbers = []
#
# for i in range(first_value, max_value + 1, first_value):
#
#     numbers.append(i)
#
# print(numbers)


factor = int(input())
count = int(input())
result = []
value = factor

for i in range(count):
    result.append(value)
    value += factor

print(result)
