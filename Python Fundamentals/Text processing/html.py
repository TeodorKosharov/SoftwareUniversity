title = input()
article = input()

print('<h1>')
print(f'   {title}')
print('</h1>')
print('<article>')
print(f'   {article}')
print('</article>')

while True:
    inp = input()
    if inp == 'end of comments':
        exit()

    print('<div>')
    print(f'   {inp}')
    print('</div>')
