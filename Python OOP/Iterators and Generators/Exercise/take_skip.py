class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_position = 0 - step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            self.current_position += self.step
            return self.current_position

        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
