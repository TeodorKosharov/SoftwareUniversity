value = input()

max_value = sorted(value, reverse=True)

for i, digit in enumerate(max_value):
    print(digit, end="")
