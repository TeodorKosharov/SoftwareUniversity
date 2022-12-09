from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from testing_demos.web.models import Profile

UserModel = get_user_model()


class ProfileListViewTest(TestCase):
    def test_profiles_list_view__when_no_profiles__expect_empty_list_and_count_context(self):
        # self.client.get() makes HTTP GET request
        response = self.client.get(reverse('list profiles'))
        self.assertListEqual([], list(response.context['profile_list']))
        self.assertEqual(0, response.context['profiles_count'])

    def test_profiles_list_view__when_profiles__expect_list_of_profiles_and_header(self):
        profiles = [
            Profile(name=f'Test user {i}', age=20 + i, egn=f'123456754{i}') for i in range(1, 11)
        ]

        Profile.objects.bulk_create(profiles)
        response = self.client.get(reverse('list profiles'))

        # profile_list == object_list
        self.assertListEqual(profiles, list(response.context['profile_list']))

    def test_profiles_list_view__when_loggedin_user__username_to_be_correct(self):
        username = 'teodor'
        password = '123'
        credentials = {
            'username': username,
            'password': password
        }

        UserModel.objects.create_user(username=username, password=password)
        self.client.login(**credentials)
        response = self.client.get(reverse('list profiles'))
        self.assertEqual(username, response.context['username'])

