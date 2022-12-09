inp = input()

digits = ''
letters = ''
others = ''

for i, symbol in enumerate(inp):

    if symbol.isalpha():
        letters += symbol
        continue

    elif symbol.isdigit():
        digits += symbol
        continue

    else:
        others += symbol

print(int(digits))
print(letters)
print(others)
