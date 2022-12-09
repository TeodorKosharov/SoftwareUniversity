inp = input()

result = ''
string_to_repeat = ''
repeat_times = ''

for index in range(len(inp)):
    char = inp[index]

    if index == len(inp) - 1 and not char.isdigit():
        result += char
        break
    elif index == len(inp) - 1 and char.isdigit():
        repeat_times += char
        result += int(repeat_times) * string_to_repeat
        break

    if not char.isdigit():
        string_to_repeat += char
    else:
        repeat_times += char
        if not inp[index + 1].isdigit():
            result += int(repeat_times) * string_to_repeat
            string_to_repeat = ''
            repeat_times = ''

result = result.upper()
uniq_chars = set(result)
print(f"Unique symbols used: {len(uniq_chars)}")
print(result)
