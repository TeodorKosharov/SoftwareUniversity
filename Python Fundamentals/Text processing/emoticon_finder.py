inp = input()

for index, symbol in enumerate(inp):
    if symbol == ':':
        print(symbol + inp[index + 1])
