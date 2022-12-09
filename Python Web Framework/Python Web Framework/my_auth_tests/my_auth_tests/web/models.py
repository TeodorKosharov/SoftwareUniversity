from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

UserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    price = models.FloatField(null=False, blank=False)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
