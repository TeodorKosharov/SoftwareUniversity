from project.library import Library
import unittest


class LibraryTest(unittest.TestCase):
    def test_constructor(self):
        sample = Library('test')
        self.assertEqual('test', sample.name)
        self.assertEqual({}, sample.books_by_authors)
        self.assertEqual({}, sample.readers)

    def test_name_property(self):
        with self.assertRaises(ValueError) as error:
            sample = Library('')
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book_method_when_both_author_and_book_are_absent(self):
        sample = Library('test')
        sample.add_book('test 1', 'test 2')
        self.assertEqual({'test 1': ['test 2']}, sample.books_by_authors)

    def test_add_book_method_when_book_is_absent(self):
        sample = Library('test')
        sample.books_by_authors = {'test 1': ['test 2']}
        sample.add_book('test 1', 'test 3')
        self.assertEqual({'test 1': ['test 2', 'test 3']}, sample.books_by_authors)

    def test_add_reader_method_when_reader_is_not_present(self):
        sample = Library('test')
        sample.add_reader('test 1')
        self.assertEqual({'test 1': []}, sample.readers)

    def test_add_reader_method_when_reader_is_present(self):
        sample = Library('test')
        sample.readers = {'test 1': []}
        result = sample.add_reader('test 1')
        self.assertEqual(f"test 1 is already registered in the test library.", result)

    def test_rent_book_method_when_reader_is_not_present(self):
        sample = Library('test')
        result = sample.rent_book('test 1', 'test 2', 'test 3')
        self.assertEqual(f"test 1 is not registered in the test Library.", result)

    def test_rent_book_method_when_book_author_is_not_present(self):
        sample = Library('test')
        sample.readers = {'test 1': []}
        result = sample.rent_book('test 1', 'test 2', 'test 3')
        self.assertEqual(f"test Library does not have any test 2's books.", result)

    def test_rent_book_method_when_book_title_is_not_present_in_authors_books(self):
        sample = Library('test')
        sample.readers = {'test 1': []}
        sample.books_by_authors = {'test 2': []}
        result = sample.rent_book('test 1', 'test 2', 'test 3')
        self.assertEqual(f"""test Library does not have test 2's "test 3".""", result)

    def test_rent_method_when_everythin_is_present(self):
        sample = Library('test')
        sample.readers = {'test 1': []}
        sample.books_by_authors = {'test 2': ['test 3']}
        sample.rent_book('test 1', 'test 2', 'test 3')
        self.assertEqual({'test 1': [{'test 2': 'test 3'}]}, sample.readers)
