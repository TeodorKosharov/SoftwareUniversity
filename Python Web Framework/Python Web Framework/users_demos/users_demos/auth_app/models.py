from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users_demos.auth_app.managers import AppUserManager


# Proxy user demo:
# class AppUser(User):
#     def has_email(self):
#         return self.email or False
#
#     # Чрез proxy=True указваме, че не искаме да се прави таблица в базата при мигриране
#     class Meta:
#         proxy = True


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False, null=False, blank=False)

    # User credentials consist of 'email' and 'password'
    USERNAME_FIELD = 'email'

    objects = AppUserManager()


# One to One relationship demo:
class Profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    user = models.OneToOneField(AppUser, primary_key=True, on_delete=models.CASCADE)

