text = input()
vowels = ['a', 'A', 'o', 'O', 'i', 'I', 'e', 'E', 'u', 'U']
no_vowels = ''.join([x for x in text if x not in vowels])
print(no_vowels)
