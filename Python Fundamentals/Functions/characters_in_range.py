def characters(char1, char2):
    result = ''

    for i in range(ord(char1) + 1, ord(char2)):
        result += f'{chr(i)} '

    return result


first_char = input()
second_char = input()
final_result = characters(first_char, second_char)
print(final_result)
