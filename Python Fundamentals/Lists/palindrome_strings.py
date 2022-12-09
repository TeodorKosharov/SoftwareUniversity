# string_list = input().split()
# palindrome = input()
#
# palindromes_list = []
# found_times = 0
#
# for element in string_list:
#
#     if element == element[::-1]:
#         palindromes_list.append(element)
#         if palindrome == element:
#             found_times += 1
#
# print(palindromes_list)
# print(f"Found palindrome {found_times} times")


sequence = input().split()
palindrome = input()

print([x for x in sequence if x == x[::-1]])
print(f"Found palindrome {sequence.count(palindrome)} times")
