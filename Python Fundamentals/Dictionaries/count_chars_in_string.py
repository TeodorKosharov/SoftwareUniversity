# word = input()
# word = word.replace(' ', '')
#
# dictionary = {}
#
# for i, char in enumerate(word):
#     if char not in dictionary:
#         dictionary[char] = 1
#     else:
#         dictionary[char] += 1
#
# for key in dictionary:
#     value = dictionary[key]
#     print(f'{key} -> {value}')


word = input().replace(' ', '')
chars = {}
looked_chars = []

for current_char in word:
    if current_char not in looked_chars:
        looked_chars.append(current_char)
        chars.update({current_char: word.count(current_char)})

for key, count in chars.items():
    print(f'{key} -> {count}')
