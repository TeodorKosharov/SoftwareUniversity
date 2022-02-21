command = input()
nums = [int(x) for x in input().split()]

evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 == 1]

if command == 'Even':
    print(sum(evens) * len(nums))
else:
    print(sum(odds) * len(nums))
