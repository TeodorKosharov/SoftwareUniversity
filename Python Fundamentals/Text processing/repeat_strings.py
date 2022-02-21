inp = input().split(' ')
res = ''

for word in inp:
    n = len(word)
    res += word * n

print(res)
