from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from authentication.web.decorators import allow_groups


# Ways to create users:
# 1. python manage.py createsuperuser
# 2. From admin panel by a superuser
# 3. With code: User.objects.create_user() or User.objects.create_superuser()


@allow_groups(groups=['Users'])
def index(request):
    print(request.user)
    user_message = '' if request.user.is_authenticated else 'not'
    return HttpResponse(f'The user is {user_message} authenticated!')


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Teodor',
        password='123teo'
    )

    # login():
    # - creates the session
    # - attaches 'user' to request

    login(request, user)


def check_perms(request):
    user = User.objects.get(username='Teodor')
    admin = User.objects.get(username='teo')
    permissions = (
        'web.add_user',
        'web.change_user',
        'web.delete_user',
        'web.view_user'
    )

    [print(user.has_perm(perm)) for perm in permissions]
    [print(admin.has_perm(perm)) for perm in permissions]


# Requires 'login' in function-based view
@login_required()
def show_profile(request):
    return HttpResponse(f'You are {request.user}')


# Requires 'login' in class-based view
class ProfileView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return HttpResponse(f'You are {request.user}')
