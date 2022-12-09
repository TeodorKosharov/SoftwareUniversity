# numbers = input()
#
# list_numbers = numbers.split()
# opposite_numbers = []
#
# for symbol in list_numbers:
#     num = int(symbol)
#
#     opposite_numbers.append(-num)
#
# print(opposite_numbers)


inp = list(map(int, input().split()))
print([-x for x in inp])

