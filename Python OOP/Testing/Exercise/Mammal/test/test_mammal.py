import unittest
from Exercise.Mammal.project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def test_constuctor(self):
        sample = Mammal('test', 'test type', 'oof')
        self.assertEqual('test', sample.name)
        self.assertEqual('test type', sample.type)
        self.assertEqual('oof', sample.sound)
        self.assertEqual('animals', sample.get_kingdom())

    def test_make_sound_method(self):
        sample = Mammal('test', 'test type', 'oof')
        expected = 'test makes oof'
        actual = sample.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom_method(self):
        sample = Mammal('test', 'test type', 'oof')
        self.assertEqual('animals', sample.get_kingdom())

    def test_info_method(self):
        sample = Mammal('test', 'test type', 'oof')
        expected = 'test is of type test type'
        actual = sample.info()
        self.assertEqual(expected, actual)
