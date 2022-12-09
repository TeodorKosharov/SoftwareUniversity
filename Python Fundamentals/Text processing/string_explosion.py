inp = input()

res = ''
index = 0
explosions = 0

for i in range(len(inp)):
    char = inp[index]

    if explosions > 0:
        if char != '>':
            explosions -= 1

        elif char == '>':
            explosions += int(inp[index + 1])
            res += char
        index += 1
        continue

    if char != '>' and explosions == 0:
        res += char

    elif char == '>':
        explosions += int(inp[index + 1])
        res += char

    index += 1

print(res)
