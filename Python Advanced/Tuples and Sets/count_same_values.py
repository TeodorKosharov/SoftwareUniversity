numbers = map(float, input().split())

nums_dict = {}
for num in numbers:
    if num not in nums_dict:
        nums_dict[num] = 0
    nums_dict[num] += 1

for k in nums_dict.items():
    print(f'{k[0]:.1f} - {k[1]} times')

# for key, value in nums_dict.items():
#     print(f'{key:.1f} - {value} times')
