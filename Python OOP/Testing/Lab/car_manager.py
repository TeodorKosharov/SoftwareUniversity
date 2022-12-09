import unittest


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class CarTest(unittest.TestCase):
    def test_constructor(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        self.assertEqual('test make', sample.make)
        self.assertEqual('Mercedes', sample.model)
        self.assertEqual(20, sample.fuel_consumption)
        self.assertEqual(80, sample.fuel_capacity)
        self.assertEqual(0, sample.fuel_amount)

    def test_set_make_attribute_value_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        sample.make = 'test'
        self.assertEqual('test', sample.make)

    def test_set_make_attribute_value_with_error_condition__none_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.make = None
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_set_make_attribute_value_with_error_condition__empty_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.make = ''
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_set_model_attribute_value_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        sample.model = 'Bentley'
        self.assertEqual('Bentley', sample.model)

    def test_set_model_attribute_value_with_error_condition__none_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.model = None
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_set_model_attribute_value_with_error_condition__empty_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.model = ''
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_set_fuel_consumption_attribute_value_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        self.assertEqual(20, sample.fuel_consumption)

    def test_set_fuel_consumption_with_error_condition__negative_value(self):
        with self.assertRaises(Exception) as error:
            sample = Car('test make', 'Mercedes', -20, 80)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_set_fuel_consumption_with_error_condition__zero_value(self):
        with self.assertRaises(Exception) as error:
            sample = Car('test make', 'Mercedes', 0, 80)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_set_fuel_capacity_attribute_value_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        self.assertEqual(80, sample.fuel_capacity)

    def test_set_fuel_capacity_attribute_value_with_error_condition__negative_value(self):
        with self.assertRaises(Exception) as error:
            sample = Car('test make', 'Mercedes', 20, -80)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_set_fuel_capacity_attribute_value_with_error_condition__zero_value(self):
        with self.assertRaises(Exception) as error:
            sample = Car('test make', 'Mercedes', 20, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_set_fuel_amount_attribute_value_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        sample.fuel_amount = 10
        self.assertEqual(10, sample.fuel_amount)

    def test_set_fuel_amount_attribute_value_with_error_condition__negative_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_refuel_method_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        sample.refuel(20)
        self.assertEqual(sample.fuel_amount - 20, 0)

    def test_refuel_method_with_error_condition__negative_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_refuel_method_with_error_condition__zero_value(self):
        sample = Car('test make', 'Mercedes', 20, 80)
        with self.assertRaises(Exception) as error:
            sample.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_drive_method_without_error_condition(self):
        sample = Car('test make', 'Mercedes', 1, 80)
        sample.fuel_amount = 100
        sample.drive(100)
        self.assertEqual(99, sample.fuel_amount)

    def test_drive_method_with_error_condition(self):
        sample = Car('test make', 'Mercedes', 1, 80)
        with self.assertRaises(Exception) as error:
            sample.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(error.exception))


if __name__ == '__main__':
    unittest.main()
