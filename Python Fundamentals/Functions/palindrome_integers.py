def palindrome_check(numbers_list):
    for element in numbers_list:
        if element == element[::-1]:
            print('True')
        else:
            print('False')


numbers = input().split(', ')
palindrome_check(numbers)
