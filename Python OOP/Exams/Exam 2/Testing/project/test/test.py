import unittest
from project.student_report_card import StudentReportCard


class StudentReportCardTest(unittest.TestCase):
    def test_student_name_and_school_year__valid_case(self):
        sample = StudentReportCard('test', 5)
        self.assertEqual('test', sample.student_name)
        self.assertEqual(5, sample.school_year)

    def test_student_name__invalid_case(self):
        with self.assertRaises(ValueError) as error:
            sample = StudentReportCard('', 5)
        self.assertEqual('Student Name cannot be an empty string!', str(error.exception))

    def test_school_year_invalid_vase(self):
        with self.assertRaises(ValueError) as error:
            sample = StudentReportCard('test', 20)
        self.assertEqual('School Year must be between 1 and 12!', str(error.exception))

    def test_add_grade_method_subject_not_in_list(self):
        sample = StudentReportCard('test', 5)
        sample.grades_by_subject = {'math': [5, 5, 6]}
        sample.add_grade('biology', 5.50)
        self.assertEqual({'math': [5, 5, 6], 'biology': [5.50]}, sample.grades_by_subject)

    def test_add_grade_method_subject_in_list(self):
        sample = StudentReportCard('test', 5)
        sample.grades_by_subject = {'math': [5, 5, 6]}
        sample.add_grade('math', 5.50)
        self.assertEqual({'math': [5, 5, 6, 5.50]}, sample.grades_by_subject)

    def test_average_grade_method(self):
        sample = StudentReportCard('test', 5)
        sample.grades_by_subject = {'math': [4, 5, 6]}
        actual_result = sample.average_grade_by_subject()
        self.assertEqual(f'math: 5.00', actual_result)

    def test_average_grade_method_without_any_grades(self):
        sample = StudentReportCard('test', 5)
        actual_result = sample.average_grade_by_subject()
        self.assertEqual(f'', actual_result)

    def test_average_grade_for_all_subjects_method(self):
        sample = StudentReportCard('test', 5)
        sample.grades_by_subject = {'math': [4, 5, 6]}
        actual_result = sample.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 5.00', actual_result)

    def test_average_grade_for_all_subjects_method_without_any_grades(self):
        sample = StudentReportCard('test', 5)
        sample.grades_by_subject = {}
        with self.assertRaises(ZeroDivisionError) as error:
            sample.average_grade_for_all_subjects()
        self.assertEqual('division by zero', str(error.exception))

    def test_repr_method(self):
        sample = StudentReportCard('test', 5)
        sample.grades_by_subject = {'math': [4, 5, 6]}
        expected = f"Name: test\n" \
                   f"Year: 5\n" \
                   f"----------\n" \
                   f"math: 5.00\n" \
                   f"----------\n" \
                   f"Average Grade: 5.00"
        print(expected)
        actual = repr(sample)
        print(actual)
        self.assertEqual(expected, actual)
