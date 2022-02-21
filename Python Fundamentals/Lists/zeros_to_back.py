values = input().split(', ')

for index in range(len(values)):

    if values[index] == '0':
        values.remove(values[index])
        values.append('0')

print(list(map(int, values)))
