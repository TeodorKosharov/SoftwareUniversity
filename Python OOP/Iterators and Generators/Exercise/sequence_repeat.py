class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __validate_index(self):
        if self.index == len(self.sequence):
            self.index = 0
        return self.index

    def __iter__(self):
        return self

    def __next__(self):
        self.number -= 1
        self.index += 1

        if self.number > -1:
            return self.sequence[self.__validate_index()]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
