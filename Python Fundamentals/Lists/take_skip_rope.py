string_inp = input()

numbers_list_str = list(filter(str.isdigit, string_inp))

numbers_list = [int(x) for x in numbers_list_str]
symbols_list = [x for x in string_inp if x not in numbers_list_str]

take_list = []
skip_list = []

for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

result = ''
for x in range(len(take_list)):
    take_chars = take_list[x]
    skip_chars = skip_list[x]

    for take_symbol in range(take_chars):
        if len(symbols_list) == 0:
            break
        result += symbols_list[0]
        symbols_list.pop(0)

    for skip_symbol in range(skip_chars):
        symbols_list.pop(0)

print(result)
