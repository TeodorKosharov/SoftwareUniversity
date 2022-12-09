# First variant:

# sequence = input()
#
# stack = []
#
# for char in sequence:
#     if char == '(' or char == '{' or char == '[':
#         stack.append(char)
#     else:
#         if stack:
#             # check if the closing bracket is the same type as the bracket at the top of the stack:
#             if char == ')' and stack[-1] == '(':
#                 stack.pop()
#             elif char == '}' and stack[-1] == '{':
#                 stack.pop()
#             elif char == ']' and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 print('NO')
#                 exit()
#         else:
#             print('NO')
#             exit()
#
# print('YES')

# Second variant:

sequence = input()

stack = []

for char in sequence:
    if char in '({[':
        stack.append(char)
    else:
        if stack and f'{stack[-1]}{char}' in '(){}[]':
            stack.pop()
        else:
            print('NO')
            exit()
if stack:
    print('NO')
else:
    print('YES')
