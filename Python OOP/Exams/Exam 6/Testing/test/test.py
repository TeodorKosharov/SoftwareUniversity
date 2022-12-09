from project.team import Team
import unittest


class TeamTest(unittest.TestCase):
    def test_constructor(self):
        sample = Team('test')
        self.assertEqual('test', sample.name)
        self.assertEqual({}, sample.members)

    def test_name_property(self):
        with self.assertRaises(ValueError) as error:
            sample = Team('test1')
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member_method_without_any_records(self):
        sample = Team('test')
        result = sample.add_member()
        self.assertEqual(f"Successfully added: ", result)

    def test_add_method_with_one_record(self):
        sample = Team('test')
        result = sample.add_member(peter=10)
        self.assertEqual({'peter': 10}, sample.members)
        self.assertEqual(f"Successfully added: peter", result)

    def test_add_method_with_multiple_records(self):
        sample = Team('test')
        result = sample.add_member(peter=10, john=20, teo=30)
        self.assertEqual({'peter': 10, 'john': 20, 'teo': 30}, sample.members)
        self.assertEqual(f"Successfully added: peter, john, teo", result)

    def test_remove_member_method_with_absent_name(self):
        sample = Team('test')
        sample.members = {'peter': 10}
        result = sample.remove_member('john')
        self.assertEqual(f"Member with name john does not exist", result)

    def test_remove_member_method_with_present_name(self):
        sample = Team('test')
        sample.members = {'peter': 10}
        result = sample.remove_member('peter')
        self.assertEqual({}, sample.members)
        self.assertEqual(f"Member peter removed", result)

    def test_gt_method_expected_true_result(self):
        sample = Team('test')
        sample.members = {'peter': 10}
        sample2 = Team('testtt')
        result = sample > sample2
        self.assertEqual(True, result)

    def test_gt_method_expected_false_result(self):
        sample = Team('test')
        sample2 = Team('testtt')
        sample2.members = {'peter': 10}
        result = sample > sample2
        self.assertEqual(False, result)

    def test_len_method(self):
        sample = Team('test')
        sample.members = {'peter': 10}
        result = len(sample)
        self.assertEqual(1, result)

    def test_add_method(self):
        sample = Team('test')
        sample2 = Team('newtest')
        result = sample + sample2
        self.assertEqual('testnewtest', result.name)
        self.assertEqual({}, result.members)

    def test_str_method_without_any_records(self):
        sample = Team('test')
        result = str(sample)
        self.assertEqual('Team name: test', result)

    def test_str_method_with_some_records(self):
        sample = Team('test')
        sample.members = {'peter': 10}
        result = str(sample)
        self.assertEqual('Team name: test\nMember: peter - 10-years old', result)

