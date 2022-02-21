import re

while True:

    inp = input()
    if inp == '':
        break

    x = re.finditer(r'\d+', inp)
    for i in x:
        print(i.group(), end=' ')
