n = int(input())

odd_numbers = set()
even_numbers = set()

for row in range(1, n + 1):
    name = input()
    result = 0

    for char in name:
        result += ord(char)

    result //= row

    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)

if sum(odd_numbers) == sum(even_numbers):
    print(*(odd_numbers.union(even_numbers)), sep=', ')
elif sum(odd_numbers) > sum(even_numbers):
    print(*(odd_numbers.difference(even_numbers)), sep=', ')
else:
    print(*(odd_numbers.symmetric_difference(even_numbers)), sep=', ')
