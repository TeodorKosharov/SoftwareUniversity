# from sys import maxsize
#
# numbers = input()
# n = int(input())
#
# smallest = maxsize
#
# list_numbers = numbers.split()
# list_ints = list(map(int, list_numbers))
#
# for loop in range(n):
#     for element in list_ints:
#
#         if element < smallest:
#             smallest = element
#
#     list_ints.remove(smallest)
#     smallest = maxsize
#
# final_list = list(map(str, list_ints))
# print(', '.join(final_list))


integers = list(map(int, input().split()))
count = int(input())

for _ in range(count):
    integers.pop(integers.index(min(integers)))

print(', '.join(list(map(str, integers))))
