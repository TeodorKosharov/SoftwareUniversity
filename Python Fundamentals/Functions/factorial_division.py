from math import factorial


def factorial_value(num1, num2):
    first_result = factorial(num1)
    second_result = factorial(num2)
    final_result = first_result / second_result

    return format(final_result, '.2f')


first_number = int(input())
second_number = int(input())
output = factorial_value(first_number, second_number)
print(output)
