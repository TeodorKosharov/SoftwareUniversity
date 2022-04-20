from project.student import Student
import unittest


class StudentTest(unittest.TestCase):
    def test_constructor(self):
        sample = Student('test')
        self.assertEqual('test', sample.name)
        self.assertEqual({}, sample.courses)

    def test_constructor_if_courses_is_not_none(self):
        sample = Student('test', 'not none')
        self.assertEqual('test', sample.name)
        self.assertEqual('not none', sample.courses)

    def test_enroll_method_first_if_condition(self):
        sample = Student('test')
        sample.courses = {'test': []}
        result = sample.enroll('test', '111')
        self.assertEqual({'test': ['1', '1', '1']}, sample.courses)
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_enroll_method_second_if_condition__y(self):
        sample = Student('test')
        result = sample.enroll('test', '111', 'Y')
        self.assertEqual({'test': '111'}, sample.courses)
        self.assertEqual('Course and course notes have been added.', result)

    def test_enroll_method_second_if_condition__empty_string(self):
        sample = Student('test')
        result = sample.enroll('test', '111')
        self.assertEqual({'test': '111'}, sample.courses)
        self.assertEqual('Course and course notes have been added.', result)

    def test_enroll_method_final_state(self):
        sample = Student('test')
        result = sample.enroll('test1', '123', 'notes')
        sample.courses['test1'] = []
        self.assertEqual(sample.courses['test1'], [])
        self.assertEqual('Course has been added.', result)

    def test_add_notes_method_without_exception(self):
        sample = Student('test')
        sample.courses = {'python': [1, 2, 3]}
        result = sample.add_notes('python', 4)
        self.assertEqual({'python': [1, 2, 3, 4]}, sample.courses)
        self.assertEqual('Notes have been updated', result)

    def test_add_notes_method_with_exception(self):
        sample = Student('test')
        sample.courses = {'python': [1, 2, 3]}
        with self.assertRaises(Exception) as error:
            sample.add_notes('java', 4)
        self.assertEqual('Cannot add notes. Course not found.', str(error.exception))

    def test_leave_course_method_without_exception(self):
        sample = Student('test')
        sample.courses = {'python': [1, 2, 3]}
        result = sample.leave_course('python')
        self.assertEqual('Course has been removed', result)
        self.assertEqual({}, sample.courses)

    def test_leave_course_method_with_exception(self):
        sample = Student('test')
        sample.courses = {'python': [1, 2, 3]}
        with self.assertRaises(Exception) as error:
            sample.leave_course('java')
        self.assertEqual('Cannot remove course. Course not found.', str(error.exception))
