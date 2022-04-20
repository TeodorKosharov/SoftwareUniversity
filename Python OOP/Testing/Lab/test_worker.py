import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    valid_name = 'Worker 1'
    valid_salary = 1000
    valid_energy = 5

    def test_valid_name_salary_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_if_energy_is_incremented_after_calling_rest_method(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.rest()
        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_negative_energy_or_zero_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual('Not enough energy.', str(context.exception))

    def test_money_increase(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        self.assertEqual(self.valid_salary, worker.money)

    def test_decreased_energy_after_work_method(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        self.assertEqual(self.valid_energy - 1, worker.energy)

    def test_get_info_method(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected = f'{self.valid_name} has saved 0 money.'
        actual = worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
