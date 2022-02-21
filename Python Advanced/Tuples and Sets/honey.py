from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar_stack = list(map(int, input().split()))
operators = deque(input().split())

total_honey = 0

while nectar_stack and working_bees:
    current_bee = working_bees[0]
    current_nectar = nectar_stack[-1]

    if current_nectar < current_bee:
        nectar_stack.pop()
        continue

    elif current_nectar >= current_bee:
        current_operator = operators.popleft()
        if current_operator == '+':
            total_honey += current_bee + current_nectar
        elif current_operator == '-':
            total_honey += abs(current_bee - current_nectar)
        elif current_operator == '*':
            total_honey += current_bee * current_nectar
        elif current_operator == '/':
            if current_nectar == 0:
                nectar_stack.pop()
                working_bees.popleft()
                continue
            total_honey += current_bee / current_nectar
        nectar_stack.pop()
        working_bees.popleft()

print(f"Total honey made: {total_honey}")

if working_bees:
    print('Bees left: ', end='')
    print(*working_bees, sep=', ')

if nectar_stack:
    print('Nectar left: ', end='')
    print(*nectar_stack, sep=', ')
