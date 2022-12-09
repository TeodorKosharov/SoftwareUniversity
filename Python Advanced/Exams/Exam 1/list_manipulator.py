def list_manipulator(nums: list, *args):
    second_param = args[0]
    third_param = args[1]
    extracted_nums = [x for x in args if type(x) == int]

    if second_param == 'add':
        if third_param == 'beginning':
            return extracted_nums + nums
        else:
            return nums + extracted_nums
    else:
        if third_param == 'beginning':
            if extracted_nums:
                for i in range(extracted_nums[0]):
                    nums.pop(0)
                return nums
            else:
                return nums[1:]
        else:
            if extracted_nums:
                for i in range(extracted_nums[0]):
                    nums.pop(-1)
                return nums
            else:
                return nums[0: -1]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
