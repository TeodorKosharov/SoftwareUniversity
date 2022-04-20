from project.movie import Movie
import unittest


class MovieTest(unittest.TestCase):
    def test_constuctor(self):
        sample = Movie('test', 2001, 5.5)
        self.assertEqual('test', sample.name)
        self.assertEqual(2001, sample.year)
        self.assertEqual(5.5, sample.rating)

    def test_name_property(self):
        with self.assertRaises(ValueError) as error:
            sample = Movie('', 2001, 5.5)
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_property(self):
        with self.assertRaises(ValueError) as error:
            sample = Movie('test', 1001, 5.5)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_method_when_actor_name_is_not_present(self):
        sample = Movie('test', 2001, 5.5)
        sample.add_actor('Peter')
        self.assertEqual(['Peter'], sample.actors)

    def test_add_actor_method_when_actor_name_is_present(self):
        sample = Movie('test', 2001, 5.5)
        sample.add_actor('Peter')
        result = sample.add_actor('Peter')
        self.assertEqual("Peter is already added in the list of actors!", result)

    def test_greater_than_method(self):
        sample = Movie('test', 2001, 5.5)
        other = Movie('test2', 2002, 6.7)
        result = sample > other
        self.assertEqual(f'"test2" is better than "test"', result)

    def test_greater_than_method__second_variant(self):
        sample = Movie('test', 2001, 7.5)
        other = Movie('test2', 2002, 6.7)
        result = sample > other
        self.assertEqual(f'"test" is better than "test2"', result)

    def test_repr_method(self):
        sample = Movie('test', 2001, 5.5)
        sample.actors = ['Teodor', 'Plamen']
        result = repr(sample)
        expected = f"Name: test\n" \
                   f"Year of Release: 2001\n" \
                   f"Rating: 5.50\n" \
                   f"Cast: Teodor, Plamen"
        self.assertEqual(expected, result)
