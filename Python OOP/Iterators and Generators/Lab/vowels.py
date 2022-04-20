class vowels:
    def __init__(self, some_string):
        self.some_string = some_string
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.index + 1 < len(self.some_string):
            self.index += 1
            if self.some_string[self.index].upper() in 'AEIOUY':
                return self.some_string[self.index]
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
