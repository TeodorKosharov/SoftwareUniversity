import re

inp = input()
pattern = r'(?<=\b_)[a-zA-Z0-9]+\b'

x = re.finditer(pattern, inp)
res = []

for i in x:
    res.append(i.group())

print(','.join(res))
