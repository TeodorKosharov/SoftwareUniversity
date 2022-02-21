string = input()

capitals_list = []
i = 0

for symbol in string:

    if symbol.isupper():
        capitals_list.append(i)

    i += 1

print(capitals_list)
