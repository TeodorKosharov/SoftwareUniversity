from Exercise.Vehicle.project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    def test_constructor(self):
        sample = Vehicle(1.25, 120.25)
        self.assertEqual(1.25, sample.fuel)
        self.assertEqual(sample.capacity, sample.fuel)
        self.assertEqual(120.25, sample.horse_power)
        self.assertEqual(1.25, sample.fuel_consumption)

    def test_drive_method_without_exception(self):
        sample = Vehicle(100, 120.25)
        sample.drive(10)
        self.assertEqual(100 - 12.5, sample.fuel)

    def test_drive_method_with_exception(self):
        sample = Vehicle(10, 120.25)
        with self.assertRaises(Exception) as error:
            sample.drive(10)
        self.assertEqual('Not enough fuel', str(error.exception))

    def test_refuel_method_without_exception(self):
        sample = Vehicle(1.25, 120.25)
        sample.refuel(0)
        self.assertEqual(1.25, sample.fuel)

    def test_refuel_method_with_exception(self):
        sample = Vehicle(1.25, 120.25)
        with self.assertRaises(Exception) as error:
            sample.refuel(10)
        self.assertEqual('Too much fuel', str(error.exception))

    def test_str_dunder_method(self):
        sample = Vehicle(10, 200)
        expected = f"The vehicle has 200 horse power with 10 fuel left and 1.25 fuel consumption"
        actual = str(sample)
        self.assertEqual(expected, actual)
