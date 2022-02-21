# words = input().split(' ')
# lower_case_words = [w.lower() for w in words]
# dictionary = {}
#
# for word in lower_case_words:
#     if word not in dictionary:
#         dictionary[word] = 1
#     else:
#         dictionary[word] += 1
#
# for element in dictionary:
#     value = dictionary[element]
#     if value % 2 == 1:
#         print(element, end=' ')


words = [x.lower() for x in input().split()]
dictionary = {}

for element in words:
    if element not in dictionary and words.count(element) % 2 == 1:
        dictionary.update({element: words.count(element)})

print(' '.join([x for x in dictionary.keys()]))
