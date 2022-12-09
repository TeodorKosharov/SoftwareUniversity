from math import floor


def evaluator(nums: list, given_operator: str):
    result = ''
    for value in nums:
        result += value + given_operator

    if given_operator == '/':
        return floor(eval(result[0:-1]))

    return eval(result[0:-1])


expression = input().split()
nums_so_far = []
possible_operators = ['+', '-', '*', '/']

for char in expression:
    if char not in possible_operators:
        nums_so_far.append(char)
    else:
        nums_so_far = [str(evaluator(nums_so_far, char))]

print(nums_so_far[0])
