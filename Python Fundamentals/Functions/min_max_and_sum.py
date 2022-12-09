def func(nums_list):
    print(f"The minimum number is {min(nums_list)}")
    print(f"The maximum number is {max(nums_list)}")
    print(f"The sum number is: {sum(nums_list)}")


string = input().split()
numbers = list(map(int, string))
func(numbers)
