a = int(input())
b = int(input())
c = int(input())

nums_list = [a, b, c]
negatives = 0
is_zero = False

for value in nums_list:
    if value < 0:
        negatives += 1
    if value == 0:
        is_zero = True

if is_zero:
    print('zero')
    exit()

if negatives == 1 or negatives == 3:
    print('negative')
else:
    print('positive')
