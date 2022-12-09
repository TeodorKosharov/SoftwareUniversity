def even_nums_sum(value):
    if value % 2 == 0:
        return True

    return False


string = input().split()
numbers_list = list(map(int, string))

extracted_numbers = filter(even_nums_sum, numbers_list)
result = list(extracted_numbers)
print(result)

