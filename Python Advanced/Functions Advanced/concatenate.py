def concatenate(*args):
    result = ""
    for el in args:
        result += el
    return result


print(concatenate("I", " ", "Love", " ", "Python"))
