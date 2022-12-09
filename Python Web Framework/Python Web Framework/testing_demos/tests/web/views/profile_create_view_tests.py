from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile

UserModel = get_user_model()


class ProfileCreateViewTests(TestCase):
    def test_create_profile__when_user_is_loggedin__expect_to_create_profile(self):
        profile_data = {
            'name': 'Teodor',
            'age': 21,
            'egn': '1234567890'
        }

        credentials = {
            'username': 'teodor',
            'password': '123'
        }

        UserModel.objects.create_user(credentials)
        self.client.login(**credentials)
        self.client.post(reverse('create profile'), data=profile_data)
        created_profile = Profile.objects.filter(**profile_data).get()
        self.assertIsNotNone(created_profile)

