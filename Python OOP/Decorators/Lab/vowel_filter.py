def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = []
        for letter in result:
            if letter in 'aeiouy':
                vowels.append(letter)
        return vowels

    return wrapper


# Test code:

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
