def numbers_searching(*args):
    duplicates = []
    missing_value = 0
    for num in args:
        if args.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    duplicates.sort()

    sorted_args = sorted(set(args))

    for index in range(len(sorted_args) - 1):
        next_num = sorted_args[index] + 1
        if next_num != sorted_args[index + 1]:
            missing_value = next_num
            break

    return [missing_value, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
