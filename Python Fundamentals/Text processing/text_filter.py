banned_words = input().split(', ')
text = input()

for banned_word in banned_words:
    if banned_word in text:
        replace_word = '*' * len(banned_word)
        text = text.replace(banned_word, replace_word)

print(text)
