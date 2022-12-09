from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator


def validate_username(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_car_year(value):
    if not (1980 <= value <= 2049):
        raise ValidationError('Year must be between 1980 and 2049')


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, max_length=10, validators=[validate_username])
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(18)])
    password = models.CharField(null=False, blank=False, max_length=30)
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    profile_picture = models.URLField(null=True, blank=True)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name and not self.last_name:
            return self.first_name
        elif self.last_name and not self.first_name:
            return self.last_name
        return None


class Car(models.Model):
    type = models.CharField(null=False, blank=False, max_length=10, choices=[
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    ])
    model = models.CharField(null=False, blank=False, max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(null=False, blank=False, validators=[validate_car_year])
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(1)])
