expression = input()
par_stack = []

for index in range(0, len(expression)):
    if expression[index] == '(':
        par_stack.append(index)
    elif expression[index] == ')':
        start_index = par_stack.pop()
        print(expression[start_index: index + 1])
