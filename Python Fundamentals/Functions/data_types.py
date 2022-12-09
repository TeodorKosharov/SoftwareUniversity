def func(inp1, inp2):
    if inp1 == 'int':
        return int(inp2) * 2

    elif inp1 == 'real':
        return format(float(inp2) * 1.5, '.2f')

    elif inp1 == 'string':
        return f'${inp2}$'


first_input = input()
second_input = input()

result = func(first_input, second_input)
print(result)
