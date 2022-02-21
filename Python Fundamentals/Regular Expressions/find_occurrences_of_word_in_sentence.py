import re

inp = input()
search_word = input()

pattern = r'((?<=\s)|^)' + search_word + r'\b'

x = re.finditer(pattern, inp, re.IGNORECASE)
res = []
for i in x:
    res.append(i.group())

print(len(res))
