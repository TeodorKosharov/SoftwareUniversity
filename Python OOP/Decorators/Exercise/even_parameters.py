# def even_parameters(function):
#     def wrapper(*args):
#         if all([type(x) == int and x % 2 == 0 for x in args]):
#             return function(*args)
#         else:
#             return 'Please use only even numbers!'
#
#     return wrapper


def even_parameters(function):
    def wrapper(*args):
        condition = False
        for i in args:
            if type(i) == int and i % 2 == 0:
                condition = True
            else:
                condition = False
                break
        if condition or not args:
            return function(*args)
        else:
            return 'Please use only even numbers!'

    return wrapper


@even_parameters
def func():
    return "hi"


result = func()
print(result)
