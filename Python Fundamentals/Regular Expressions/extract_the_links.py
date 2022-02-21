import re

pattern = r'www.[A-Za-z0-9\-]+\.[a-z\-]+[\.[a-z\-]+\b'

while True:
    inp = input()
    if inp == '':
        break

    match = re.finditer(pattern, inp)
    for i in match:
        print(i.group())
