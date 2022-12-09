from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import mixins, get_user_model

from users_demos.auth_app.models import AppUser

UserModel = get_user_model()


class UsersListView(mixins.LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['has_email'] = AppUser.has_email(self.request.user)

        return context
