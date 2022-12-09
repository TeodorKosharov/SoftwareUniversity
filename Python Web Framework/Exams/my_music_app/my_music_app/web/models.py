from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_username(value: str):
    for char in value:
        if not char.isalnum() and not char == '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, max_length=15, validators=(
        MinLengthValidator(2),
        validate_username,
    ))
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True, validators=(MinValueValidator(0),))


class Album(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=30)
    artist = models.CharField(null=False, blank=False, max_length=30)
    genre = models.CharField(null=False, blank=False, max_length=30, choices=(
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ))
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=(
        MinValueValidator(0.0),
    ))
