from django.core.exceptions import ValidationError

from testing_demos.web.models import Profile

from django.test import TestCase


class ProfileModelTests(TestCase):
    def test_profile_save__when_egn_is_valid__expect_correct_result(self):
        profile = Profile(
            name='Teodor',
            age=21,
            egn='1234567890'
        )

        profile.full_clean()  # Call this for validation
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_egn_has_9_digits__expect_exception(self):
        profile = Profile(
            name='Teodor',
            age=21,
            egn='123456789'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

