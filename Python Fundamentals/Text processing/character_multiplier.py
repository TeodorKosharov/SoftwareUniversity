inp = input().split()

first_string = inp[0]
second_string = inp[1]

total_sum = 0

while 1:

    if len(first_string) > 0 and len(second_string) > 0:
        total_sum += ord(first_string[0]) * ord(second_string[0])
        first_string = first_string.replace(first_string[0], '', 1)
        second_string = second_string.replace(second_string[0], '', 1)

    if len(first_string) == 0:
        for symbol in second_string:
            total_sum += ord(symbol)
        break

    elif len(second_string) == 0:
        for symbol in first_string:
            total_sum += ord(symbol)
        break

print(total_sum)
