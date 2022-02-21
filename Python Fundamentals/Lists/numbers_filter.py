n = int(input())

all_values = []
filtered = []

for i in range(n):
    value = int(input())
    all_values.append(value)

command = input()

for i in all_values:
    if (command == "even" and i % 2 == 0 or i == 0) \
            or (command == "odd" and i % 2 == 1) \
            or (command == "positive" and i >= 0) \
            or (command == "negative" and i < 0):
        filtered.append(i)

print(filtered)
