b = int(input())

if b > 1:
    for i in range(2, (b // 2) + 1):
        if b % i == 0:
            is_prime = False  # Не е просто число
            break
    else:
        is_prime = True  # Просто число
else:
    is_prime = False

print(is_prime)
