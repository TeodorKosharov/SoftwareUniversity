import re


def get_word_list(given_match):
    if '#' in given_match:
        result_list = given_match.split('#')
    elif '@' in given_match:
        result_list = given_match.split('@')
    return result_list


inp = input()
total_pairs = 0
mirror_pairs = {}

pattern = r'(?P<sep>@|#)([A-Za-z]{3,})(?P=sep)(?P=sep)([A-Za-z]{3,})(?P=sep)'

matches = re.finditer(pattern, inp)

for match in matches:
    total_pairs += 1
    current_match = match.group()
    result = get_word_list(current_match)
    first_word = result[1]
    second_word = result[3]
    if first_word == second_word[::-1]:
        mirror_pairs[first_word] = second_word

if total_pairs > 0:
    print(f"{total_pairs} word pairs found!")
elif total_pairs == 0:
    print("No word pairs found!")

final_result = []

if mirror_pairs:
    for first, second in mirror_pairs.items():
        final_result.append(f'{first} <=> {second}')
else:
    print("No mirror words!")
    exit()

print('The mirror words are:')
print(', '.join(final_result))
