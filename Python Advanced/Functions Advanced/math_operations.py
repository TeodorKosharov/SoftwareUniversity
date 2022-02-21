from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    element = 1

    while nums:
        current_number = nums.popleft()
        if element == 1:
            kwargs['a'] = kwargs['a'] + current_number

        if element == 2:
            kwargs['s'] = kwargs['s'] - current_number

        if element == 3 and current_number != 0:
            kwargs['d'] = kwargs['d'] / current_number

        if element == 4:
            kwargs['m'] = kwargs['m'] * current_number

        element += 1
        if element == 5:
            element = 1

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
