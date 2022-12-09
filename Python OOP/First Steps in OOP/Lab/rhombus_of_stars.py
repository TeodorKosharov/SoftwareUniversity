# n = int(input())
#
# for i in range(1, n + 1):
#     print(' ' * (n - i) + i * '* ')
#
# for j in range(n - 1, 0, -1):
#     print(' ' * (n - j) + j * '* ')
#

# Functions approach:

def print_upper_part(num):
    for i in range(1, num + 1):
        print(' ' * (num - i) + i * '* ')


def print_bottom_part(num):
    for i in range(num - 1, 0, -1):
        print(' ' * (num - i) + i * '* ')


n = int(input())
print_upper_part(n)
print_bottom_part(n)
