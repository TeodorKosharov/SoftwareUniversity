# n = int(input())
#
# dictionary = {}
#
# for i in range(n):
#     word = input()
#     synonym = input()
#
#     if word in dictionary:
#         dictionary[word].append(synonym)
#     else:
#         dictionary[word] = [synonym]
#
# for element in dictionary:
#     values = dictionary[element]
#     res = ', '.join(values)
#     print(f'{element} - {res}')


n = int(input())
result = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in result:
        result.update({word: [synonym]})
    else:
        result[word].append(synonym)

for k, v in result.items():
    print(f'{k} - {", ".join(v)}')
