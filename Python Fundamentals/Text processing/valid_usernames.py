inp = input().split(', ')
valid_usernames = []
is_valid = False

for username in inp:
    if not (3 <= len(username) <= 16):
        continue

    if username.isalnum() or '_' in username or '-' in username:
        valid_usernames.append(username)

for i in valid_usernames:
    print(i)
