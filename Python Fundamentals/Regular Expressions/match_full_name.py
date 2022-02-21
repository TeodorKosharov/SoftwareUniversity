import re

inp = input()

pattern = r'\b([A-Z][a-z]+) ([A-Z][a-z]+)\b'
x = re.findall(pattern, inp)

for i in x:
    print(i[0], i[1], end=' ')
