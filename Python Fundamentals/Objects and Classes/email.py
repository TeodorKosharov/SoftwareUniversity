class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
while True:
    command = input()
    if command == 'Stop':
        break

    command_list = command.split()
    s = command_list[0]  # sender
    r = command_list[1]  # receiver
    c = command_list[2]  # content

    email = Email(s, r, c)
    emails.append(email)

indexes = [int(x) for x in input().split(', ')]

for i in range(len(emails)):
    current_email = emails[i]

    if i in indexes:
        current_email.send()

    current_email_info = current_email.get_info()
    print(current_email_info)
