from sys import maxsize

divisor = int(input())
boundary = int(input())

max_value = -maxsize
value = 0

for i in range(1, boundary + 1):

    if i % divisor == 0:
        value = i

    if value > max_value:
        max_value = value

print(max_value)
