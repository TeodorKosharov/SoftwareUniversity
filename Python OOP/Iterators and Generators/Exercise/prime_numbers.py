def get_primes(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
