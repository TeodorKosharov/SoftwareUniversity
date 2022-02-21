def letter_position(letter: str):
    if letter.islower():
        position = ord(letter) - 96
    else:
        position = ord(letter) - 64

    return position


inp = input().split()

suma = 0
result = 0

for element in inp:
    letter_before = element[0]
    letter_after = element[-1]
    number = ''.join([char for char in element if char.isdigit()])
    number = int(number)

    position_before = letter_position(letter_before)
    position_after = letter_position(letter_after)

    if letter_before.isupper():
        result = number / position_before
    elif letter_before.islower():
        result = number * position_before

    if letter_after.isupper():
        result -= position_after
    elif letter_after.islower():
        result += position_after

    suma += result

print(f'{suma:.2f}')
