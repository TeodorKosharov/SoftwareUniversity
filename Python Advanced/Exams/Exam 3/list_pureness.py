from collections import deque
from sys import maxsize


def best_list_pureness(nums: deque, rotations: int):
    nums = deque(nums)
    total_rotations = 0
    best_pureness = -maxsize
    best_rotation = 0

    for rotation in range(rotations + 1):
        current_pureness = 0
        for index in range(len(nums)):
            current_pureness += nums[index] * index

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = total_rotations

        total_rotations += 1
        nums.appendleft(nums.pop())

    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([-1, -2, -3, -4, -5], 2)
result = best_list_pureness(*test)
print(result)
