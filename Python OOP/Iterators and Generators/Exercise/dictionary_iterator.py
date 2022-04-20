class dictionary_iter:
    def __init__(self, some_dict):
        self.some_dict = some_dict
        self.index = -1

    def __get_dict_items(self):
        return [x for x in self.some_dict.items()]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.__get_dict_items()):
            return self.__get_dict_items()[self.index]
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
