def sum_even_odd(value):
    sum_even = 0
    sum_odd = 0

    for i, symbol in enumerate(value):
        digit = int(symbol)

        if digit % 2 == 0:
            sum_even += digit
        elif digit % 2 == 1:
            sum_odd += digit

    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = input()
result = sum_even_odd(number)
print(result)
