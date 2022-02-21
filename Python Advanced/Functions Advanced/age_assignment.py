def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        if name[0] in kwargs:
            result[name] = kwargs[name[0]]
    return result


print(age_assignment("Peter", "George", G=26, P=19))
