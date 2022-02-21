string_inp = input().split(', ')
all_numbers = list(map(int, string_inp))

positives = [number for number in all_numbers if number >= 0]
negatives = [number for number in all_numbers if number < 0]
evens = [number for number in all_numbers if number % 2 == 0]
odds = [number for number in all_numbers if number % 2 == 1]

positives_len = len(positives)
negatives_len = len(negatives)
evens_len = len(evens)
odds_len = len(odds)

print('Positive:', end=' ')
for positive in positives:
    print(positive, end='')
    positives_len -= 1
    if positives_len > 0:
        print(', ', end='')

print()
print('Negative:', end=' ')
for negative in negatives:
    print(negative, end='')
    negatives_len -= 1
    if negatives_len > 0:
        print(', ', end='')

print()
print('Even:', end=' ')
for even in evens:
    print(even, end='')
    evens_len -= 1
    if evens_len > 0:
        print(', ', end='')

print()
print('Odd:', end=' ')
for odd in odds:
    print(odd, end='')
    odds_len -= 1
    if odds_len > 0:
        print(', ', end='')
