string = input().split()

numbers = list(map(float, string))

abs_numbers = []

for value in numbers:
    abs_numbers.append(abs(value))

print(abs_numbers)
