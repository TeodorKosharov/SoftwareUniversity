from collections import deque

vowels = deque(x for x in input().split())
consonants = input().split()

search_words = {
    'rose': ['r', 'o', 's', 'e'],
    'tulip': ['t', 'u', 'l', 'i', 'p'],
    'lotus': ['l', 'o', 't', 'u', 's'],
    'daffodil': ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']
}

formed_word = ''
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word, letters in search_words.items():
        if current_vowel in letters:
            search_words[word] = [x for x in search_words[word] if x != current_vowel]

        if current_consonant in letters:
            search_words[word] = [x for x in search_words[word] if x != current_consonant]

        if not search_words[word]:
            formed_word = word
            break

    if formed_word:
        break

if formed_word:
    print(f'Word found: {formed_word}')
else:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(str(x) for x in vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(str(x) for x in consonants)}')
