numbers = input().split()
string = input()

current_sum = 0
index = 0
border = len(string) - 1
total_symbols = ''
needed_symbol = ''

for element in numbers:

    for value in range(len(element)):  # element - [9992]

        current_sum += int(element[value])

    for symbol in range(current_sum + 1):

        if index > border:
            index = 0

        needed_symbol = string[index]
        index += 1

    total_symbols += needed_symbol
    string = string.replace(needed_symbol, '', 1)
    index = 0
    current_sum = 0

print(total_symbols)
