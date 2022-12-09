from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from user_test.web.managers import AppUserManager
from django.contrib.auth.models import PermissionsMixin


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, null=False, blank=False, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'


class Profile(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    user = models.OneToOneField(AppUser, primary_key=True, on_delete=models.CASCADE)
