import re

inp = input()

title_pattern = r'\<title\>(?P<main>.+)\</title\>'
body_pattern = r'<body>.+</body>'
body_remove_pattern = r'<[A-Za-z0-9(\.\"\/\=\s)?]+>'

title_match = re.finditer(title_pattern, inp)
body_match = re.finditer(body_pattern, inp)

for match in title_match:
    title = match.group('main')

for match in body_match:
    body = match.group()

body = re.sub(body_remove_pattern, '', body)

title = title.replace(r'\n', '')
body = body.replace(r'\n', '')

print(f"Title: {title}")
print(f"Content: {body}")
