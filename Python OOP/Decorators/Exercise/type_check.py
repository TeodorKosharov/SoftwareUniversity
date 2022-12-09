def type_check(passed_type):
    def decorator(function):
        def wrapper(num):
            return function(num) if passed_type == type(num) else 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
