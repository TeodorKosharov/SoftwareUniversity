import re

inp = input()

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
x = re.finditer(pattern, inp)

for element in x:
    print(element.group(), end=' ')
