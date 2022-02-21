def palindrome(word, index, check_index=-1):
    if index == len(word) // 2:  # if the index is equal to the middle index
        return f'{word} is a palindrome'

    if word[index] == word[check_index]:
        return palindrome(word, index + 1, check_index - 1)
    else:
        return f'{word} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
