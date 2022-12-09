def get_letter_from_morse(morse_string: str):
    res = ''
    if morse_string == '.-':
        res = 'A'
    elif morse_string == '-...':
        res = 'B'
    elif morse_string == '-.-.':
        res = 'C'
    elif morse_string == '-..':
        res = 'D'
    elif morse_string == '.':
        res = 'E'
    elif morse_string == '..-.':
        res = 'F'
    elif morse_string == '--.':
        res = 'G'
    elif morse_string == '....':
        res = 'H'
    elif morse_string == '..':
        res = 'I'
    elif morse_string == '.---':
        res = 'J'
    elif morse_string == '-.-':
        res = 'K'
    elif morse_string == '.-..':
        res = 'L'
    elif morse_string == '--':
        res = 'M'
    elif morse_string == '-.':
        res = 'N'
    elif morse_string == '---':
        res = 'O'
    elif morse_string == '.--.':
        res = 'P'
    elif morse_string == '--.-':
        res = 'Q'
    elif morse_string == '.-.':
        res = 'R'
    elif morse_string == '...':
        res = 'S'
    elif morse_string == '-':
        res = 'T'
    elif morse_string == '..-':
        res = 'U'
    elif morse_string == '...-':
        res = 'V'
    elif morse_string == '.--':
        res = 'W'
    elif morse_string == '-..-':
        res = 'X'
    elif morse_string == '-.--':
        res = 'Y'
    elif morse_string == '--..':
        res = 'Z'
    return res


inp = input()

inp = inp.replace(' ', ',')

morse_word = ''
result = ''

for index in range(len(inp)):

    char = inp[index]

    if '|' in inp[index:]:
        if char != ',' and char != '|':
            morse_word += char

        elif char == ',' and inp[index - 1] != '|':
            transformed_word = get_letter_from_morse(morse_word)
            result += transformed_word
            morse_word = ''

        elif char == '|':
            result += ' '

    elif '|' not in inp[index:]:
        if char == ',' and inp[index - 1] == '|':
            continue
        elif char == ',':
            transformed_word = get_letter_from_morse(morse_word)
            result += transformed_word
            morse_word = ''
        else:
            morse_word += char

transformed_word = get_letter_from_morse(morse_word)
result += transformed_word

print(result)
