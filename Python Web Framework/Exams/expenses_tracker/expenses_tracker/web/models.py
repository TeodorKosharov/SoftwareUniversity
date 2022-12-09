from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def validate_only_letters(value: str):
    if not value.isalpha():
        return ValidationError('Ensure this value contains only letters.')


@deconstructible  # Валидаторите класове трябва да имат този декоратор (Това е Django конвенция)
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError('Max file size is 5.00 MB')

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024


class Profile(models.Model):
    first_name = models.CharField(max_length=15, validators=(MinLengthValidator(2), validate_only_letters))
    last_name = models.CharField(max_length=15, validators=(MinLengthValidator(2), validate_only_letters))
    budget = models.FloatField(default=0, validators=(MinValueValidator(0),))
    profile_image = models.ImageField(null=True,
                                      blank=True,
                                      validators=(MaxFileSizeInMbValidator(5),),
                                      upload_to='profiles/')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    title = models.CharField(max_length=30)
    expense_image = models.URLField()
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()

    class Meta:
        ordering = ('title', 'price')
