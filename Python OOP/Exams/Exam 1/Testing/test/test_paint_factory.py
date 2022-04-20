import unittest
from project.factory.paint_factory import PaintFactory


class FactoryTest(unittest.TestCase):
    def test_constructor(self):
        sample = PaintFactory('test', 10)
        self.assertEqual('test', sample.name)
        self.assertEqual(10, sample.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], sample.valid_ingredients)

    def test_add_ingredient_with_valid_product_type_and_true_inner_codntion(self):
        sample = PaintFactory('test', 10)
        sample.add_ingredient('white', 10)
        self.assertEqual(10, sample.ingredients['white'])

    def test_add_ingredient_with_valid_product_type_and_false_inner_codntion(self):
        sample = PaintFactory('test', 1)
        with self.assertRaises(ValueError) as error:
            sample.add_ingredient('white', 10)
        self.assertEqual("Not enough space in factory", str(error.exception))

    def test_add_method_with_invalid_product_type(self):
        sample = PaintFactory('test', 10)
        with self.assertRaises(TypeError) as error:
            sample.add_ingredient('not valid', 10)
        self.assertEqual("Ingredient of type not valid not allowed in PaintFactory", str(error.exception))

    def test_remove_ingredient_with_valid_product(self):
        sample = PaintFactory('test', 10)
        sample.ingredients['white'] = 10
        sample.remove_ingredient('white', 5)
        self.assertEqual(5, sample.ingredients['white'])

    def test_remove_ingredient_with_valid_product_more_quantity(self):
        sample = PaintFactory('test', 10)
        sample.ingredients['white'] = 10
        with self.assertRaises(ValueError) as error:
            sample.remove_ingredient('white', 20)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test_remove_ingredient_with_invalid_product_type(self):
        sample = PaintFactory('test', 10)
        with self.assertRaises(KeyError) as error:
            sample.remove_ingredient('non valid', 10)
        self.assertEqual("No such ingredient in the factory", str(error.exception))

    def test_products_method(self):
        sample = PaintFactory('test', 10)
        result = sample.products
        self.assertEqual({}, result)
