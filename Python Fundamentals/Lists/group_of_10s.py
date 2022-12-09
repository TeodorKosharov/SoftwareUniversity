string_nums = input().split(', ')
int_nums = list(map(int, string_nums))

factor = 10
old_factor = 0

while len(int_nums) > 0:
    current_list = []

    for number in int_nums:
        if old_factor <= number <= factor:
            current_list.append(number)

    for num in current_list:
        if num in int_nums:
            int_nums.remove(num)

    print(f"Group of {factor}'s: {current_list}")
    old_factor = factor
    factor += 10

