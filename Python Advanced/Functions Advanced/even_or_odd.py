# def even_odd(*args):
#     nums = [x for x in args if type(x) == int]
#     if 'even' in args:
#         return [x for x in nums if x % 2 == 0]
#     else:
#         return [x for x in nums if x % 2 == 1]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

def even_odd(*args):
    if 'even' in args:
        return [x for x in args if type(x) == int and x % 2 == 0]
    else:
        return [x for x in args if type(x) == int and x % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
