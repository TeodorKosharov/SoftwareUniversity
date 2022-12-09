class reverse_iter:
    def __init__(self, some_data):
        self.some_data = some_data
        self.index = len(some_data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > -1:
            result = self.some_data[self.index]
            self.index -= 1
            return result
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
