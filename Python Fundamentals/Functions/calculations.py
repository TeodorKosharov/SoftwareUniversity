def operations(operator, first_value, second_value):
    if operator == 'add':
        return first_value + second_value
    elif operator == 'subtract':
        return first_value - second_value
    elif operator == 'divide':
        return first_value // second_value
    else:
        return first_value * second_value


result = operations(input(), int(input()), int(input()))
print(result)
