# First variant:

# names = input().split()
# n = int(input())
#
# index = 0
# while not len(names) == 1:
#     index -= 1
#
#     for i in range(n):
#         index += 1
#         if index > len(names) - 1:
#             index = 0
#
#     print(f'Removed {names.pop(index)}')
#
# print(f"Last is {names[0]}")


# Second variant:

from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    kids.rotate(-n)
    print(f'Removed {kids.popleft()}')

print(f'Last is {kids.popleft()}')
