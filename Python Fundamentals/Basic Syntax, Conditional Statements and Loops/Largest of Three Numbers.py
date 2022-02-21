from sys import maxsize

max_value = -maxsize

for i in range(1, 4):

    value = int(input())

    if value > max_value:
        max_value = value

print(max_value)


# Втори начин:

# first = int(input())
# second = int(input())
# third = int(input())
#
# if first > second and first > third:
#     print(first)
#
# elif second > first and second > third:
#     print(second)
#
# else:
#     print(third)
