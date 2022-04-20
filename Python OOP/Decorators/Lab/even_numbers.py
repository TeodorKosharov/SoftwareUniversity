def even_numbers(function):
    def wrapper(numbers):
        even_nums = []
        result = function(numbers)
        for num in result:
            if num % 2 == 0:
                even_nums.append(num)
        return even_nums

    return wrapper


# Test code:

@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
