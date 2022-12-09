from django.core.exceptions import ValidationError
from django.db import models


def validate_text(value):
    if '_' in value:
        raise ValidationError('underscore is invalid character')


class Person(models.Model):
    name = models.CharField(max_length=20)
    profile_image = models.ImageField(null=True, blank=True, upload_to='persons')

    def __str__(self):
        return self.name


class Todo(models.Model):
    text = models.CharField(max_length=25, validators=(validate_text,))
    priority = models.IntegerField()
    is_done = models.BooleanField(null=False, blank=False, default=False)
    assignee = models.ForeignKey(Person, on_delete=models.RESTRICT)
