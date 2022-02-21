inp = input()

res = ''
last_letter = ''

for symbol in inp:
    if symbol != last_letter:
        res += symbol
        last_letter = symbol

print(res)
