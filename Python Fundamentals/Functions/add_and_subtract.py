def sum_numbers(a, b):
    return a + b


def subtract(suma, c):
    return suma - c


def add_and_subtract(a, b, c):
    sum = sum_numbers(a, b)
    result = subtract(sum, c)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
