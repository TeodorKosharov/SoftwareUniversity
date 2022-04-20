import unittest
from project.train.train import Train


class TrainTest(unittest.TestCase):
    def test_constructor(self):
        sample = Train('test', 20)
        self.assertEqual('test', sample.name)
        self.assertEqual(20, sample.capacity)
        self.assertEqual([], sample.passengers)

    def test_add_method_without_any_exception(self):
        sample = Train('test', 20)
        actual_result = sample.add('name')
        self.assertEqual("Added passenger name", actual_result)

    def test_add_method_with_no_capacity_left(self):
        sample = Train('test', 1)
        sample.passengers = ['passenger']
        with self.assertRaises(ValueError) as error:
            sample.add('name')
        self.assertEqual("Train is full", str(error.exception))

    def test_add_method_with_passenger_already_in_list(self):
        sample = Train('test', 2)
        sample.passengers = ['passenger']
        with self.assertRaises(ValueError) as error:
            sample.add('passenger')
        self.assertEqual("Passenger passenger Exists", str(error.exception))

    def test_remove_method_without_exception(self):
        sample = Train('test', 20)
        sample.passengers = ['passenger']
        actual_result = sample.remove('passenger')
        self.assertEqual('Removed passenger', actual_result)

    def test_remove_method_with_exception(self):
        sample = Train('test', 20)
        sample.passengers = ['passenger']
        with self.assertRaises(ValueError) as error:
            sample.remove('name')
        self.assertEqual("Passenger Not Found", str(error.exception))
