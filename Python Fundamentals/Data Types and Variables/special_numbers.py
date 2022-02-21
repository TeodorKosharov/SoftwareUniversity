n = int(input())

is_special = False
digit = 0

for number in range(1, n + 1):

    current_value = str(number)

    for x in current_value:

        digit += int(x)

        if digit == 5 or digit == 7 or digit == 11:
            is_special = True
        else:
            is_special = False

    print(f"{number} -> {is_special}")
    digit = 0



# Втори начин с метода enumerate

# n = int(input())
#
# is_special = False
# suma = 0
#
# for number in range(1, n + 1):
#
#     for i, digit in enumerate(str(number)):
#
#         suma += int(digit)
#
#         if suma == 5 or suma == 7 or suma == 11:
#             is_special = True
#         else:
#             is_special = False
#
#     print(f"{number} -> {is_special}")
#     suma = 0
