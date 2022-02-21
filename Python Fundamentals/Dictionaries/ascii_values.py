# symbols = input().split(', ')
# res = {}
#
# for symbol in symbols:
#     key = symbol
#     value = ord(symbol)
#
#     res[key] = value
#
# print(res)

characters = input().split(', ')
result = {k: ord(k) for k in characters}
print(result)
