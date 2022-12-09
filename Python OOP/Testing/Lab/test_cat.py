import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):
    valid_name = 'Cat 1'

    def test_cat_size_increased_after_eating(self):
        cat = Cat(self.valid_name)
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_fed_after_eating(self):
        cat = Cat(self.valid_name)
        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_feed_already_fed_cat(self):
        cat = Cat(self.valid_name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep_if_not_fed_already(self):
        cat = Cat(self.valid_name)
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_sleepy_after_sleeping(self):
        cat = Cat(self.valid_name)
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)


if __name__ == '__main__':
    unittest.main()
