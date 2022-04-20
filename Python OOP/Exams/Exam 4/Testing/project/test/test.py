from project.pet_shop import PetShop
import unittest


class PetShopTest(unittest.TestCase):
    def test_construcotr(self):
        sample = PetShop('test')
        self.assertEqual('test', sample.name)
        self.assertEqual({}, sample.food)
        self.assertEqual([], sample.pets)

    def test_add_food_method_with_zero_quantity(self):
        sample = PetShop('test')
        with self.assertRaises(ValueError) as error:
            sample.add_food('test', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_method_with_negative_quantity(self):
        sample = PetShop('test')
        with self.assertRaises(ValueError) as error:
            sample.add_food('test', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_method_with_absent_food(self):
        sample = PetShop('test')
        sample.food = {'apple': 2}
        result = sample.add_food('pear', 2)
        self.assertEqual("Successfully added 2.00 grams of pear.", result)
        self.assertEqual({'apple': 2, 'pear': 2}, sample.food)

    def test_add_food_method_with_food_already_in_the_dict(self):
        sample = PetShop('test')
        sample.food = {'apple': 2}
        result = sample.add_food('apple', 2)
        self.assertEqual("Successfully added 2.00 grams of apple.", result)
        self.assertEqual({'apple': 4}, sample.food)

    def test_add_pet_method_without_error(self):
        sample = PetShop('test')
        result = sample.add_pet('test pet')
        self.assertEqual("Successfully added test pet.", result)
        self.assertEqual(['test pet'], sample.pets)

    def test_add_pet_method_with_error(self):
        sample = PetShop('test')
        sample.pets = ['test pet']
        with self.assertRaises(Exception) as error:
            sample.add_pet('test pet')
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_feed_pet_method_when_pet_name_not_present(self):
        sample = PetShop('test')
        with self.assertRaises(Exception) as error:
            sample.feed_pet('apple', 'test name')
        self.assertEqual("Please insert a valid pet name", str(error.exception))

    def test_feed_pet_method_when_food_name_not_present(self):
        sample = PetShop('test')
        sample.pets = ['test name']
        result = sample.feed_pet('apple', 'test name')
        self.assertEqual(f'You do not have apple', result)

    def test_feed_pet_method_when_food_is_under_100_and_passing_valid_food(self):
        sample = PetShop('test')
        sample.food = {'apple': 10}
        sample.pets = ['test pet']
        result = sample.feed_pet('apple', 'test pet')
        self.assertEqual("Adding food...", result)
        self.assertEqual({'apple': 1010.00}, sample.food)

    def test_feed_pet_method_when_food_is_under_100_and_passing_invalid_food(self):
        sample = PetShop('test')
        sample.pets = ['test pet']
        sample.food = {'apple': 0}
        result = sample.feed_pet('apple', 'test pet')
        self.assertEqual({'apple': 1000.00}, sample.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_method_with_valid_inputs(self):
        sample = PetShop('test')
        sample.pets = ['test pet']
        sample.food = {'apple': 200}
        result = sample.feed_pet('apple', 'test pet')
        self.assertEqual(f"test pet was successfully fed", result)
        self.assertEqual({'apple': 100}, sample.food)

    def test_repr_method(self):
        sample = PetShop('test')
        sample.pets = ['cat', 'dog', 'mouse']
        result = repr(sample)
        expected = 'Shop test:\n' + 'Pets: cat, dog, mouse'
        self.assertEqual(expected, result)
