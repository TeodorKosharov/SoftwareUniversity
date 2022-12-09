import re

inp = input()

pattern = r'((?<=\s)|^)([a-z0-9]+\.?\-?\_?([a-z0-9]+)?)@[a-z(\-)?]+\.[a-z(\-)?]+(\.([a-z(\-)?]+))?\b'

match = re.finditer(pattern, inp)

for i in match:
    print(i.group())
