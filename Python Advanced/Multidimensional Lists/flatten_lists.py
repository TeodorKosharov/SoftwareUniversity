inp = input().split('|')

res = []
final = []

for i in inp:
    res.append(i.split())

for index in range(len(res) - 1, -1, -1):
    final.extend(res[index])

print(*final)
