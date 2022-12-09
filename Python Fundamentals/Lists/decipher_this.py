secret_message = input().split()

final_result = ''
for word in secret_message:
    first_part = chr(int(''.join(filter(str.isdigit, word))))
    second_part = ''.join(filter(str.isalpha, word))
    result = first_part + second_part

    second_letter = result[1:2]
    last_letter = result[-1]

    for index in range(len(result)):
        if index == 1:
            final_result += last_letter
            continue
        if index == len(result) - 1:
            final_result += second_letter
            break

        final_result += result[index]

    final_result += ' '

print(final_result)
