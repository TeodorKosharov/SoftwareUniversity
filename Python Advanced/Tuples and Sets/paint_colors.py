from collections import deque

substrings = deque(input().split())

colors = ['yellow', 'blue', 'red']
secondary_colors = ['green', 'purple', 'orange']
produced_colors = []

while len(substrings) > 1:
    middle = len(substrings) // 2 - 1
    first_substring = substrings.popleft()
    last_substring = substrings.pop()

    first_possible_match = first_substring + last_substring
    second_possible_match = last_substring + first_substring

    if first_possible_match in colors:
        produced_colors.append(first_possible_match)

    elif first_possible_match in secondary_colors:
        produced_colors.append(first_possible_match)

    elif second_possible_match in colors:
        produced_colors.append(second_possible_match)

    elif second_possible_match in secondary_colors:
        produced_colors.append(second_possible_match)

    else:
        first_substring = first_substring[0:-1]
        last_substring = last_substring[0:-1]

        if last_substring != '':
            substrings.insert(middle, last_substring)
        if first_substring != '':
            substrings.insert(middle, first_substring)

if substrings and substrings[0] in colors:
    produced_colors.append(substrings[0])

for secondary_color in secondary_colors:
    if secondary_color == 'orange' and secondary_color in produced_colors:
        if 'red' not in produced_colors or 'yellow' not in produced_colors:
            produced_colors.remove('orange')

    elif secondary_color == 'purple' and secondary_color in produced_colors:
        if 'red' not in produced_colors or 'blue' not in produced_colors:
            produced_colors.remove('purple')

    elif secondary_color == 'green' and secondary_color in produced_colors:
        if 'yellow' not in produced_colors or 'blue' not in produced_colors:
            produced_colors.remove('green')

print(produced_colors)
