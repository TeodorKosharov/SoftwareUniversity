inp = input()
result = ''

for symbol in inp:
    current_ascii_position = ord(symbol)
    needed_position = current_ascii_position + 3

    result += chr(needed_position)

print(result)
