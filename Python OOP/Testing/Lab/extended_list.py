import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTest(unittest.TestCase):
    def test_constructor_and_get_data_method(self):
        sample = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], sample.get_data())

    def test_add_method_without_raise_error_condition(self):
        sample = IntegerList(1, 2, 3)
        sample.add(4)
        self.assertEqual([1, 2, 3, 4], sample.get_data())

    def test_add_method_with_raise_error_condition(self):
        sample = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            sample.add('4')
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_remove_index_method_without_error_condition(self):
        sample = IntegerList(1, 2, 3)
        removed_element = sample.remove_index(1)
        self.assertEqual(2, removed_element)

    def test_remove_index_method_with_raise_error_condition(self):
        sample = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            sample.remove_index(4)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_method_without_error_condition(self):
        sample = IntegerList(1, 2, 3)
        taken_element = sample.get(0)
        self.assertEqual(1, taken_element)

    def test_get_method_with_raise_error_condition(self):
        sample = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            sample.get(4)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_method_without_error_condition(self):
        sample = IntegerList(1, 2, 3)
        sample.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], sample.get_data())

    def test_insert_method_with_index_error(self):
        sample = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            sample.insert(4, 1)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_method_with_invalid_type_error(self):
        sample = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            sample.insert(0, '1')
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_get_biggest_method(self):
        sample = IntegerList(1, 2, 3)
        element = sample.get_biggest()
        self.assertEqual(3, element)

    def test_get_index_method(self):
        sample = IntegerList(1, 2, 3)
        result = sample.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
