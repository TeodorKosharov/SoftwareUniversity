class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            result = self.start
            self.start += 1
            return result
        raise StopIteration()


custom = custom_range(1, 10)
for i in custom:
    print(i)
