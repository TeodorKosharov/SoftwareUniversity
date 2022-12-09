from django.db import models


class Profile(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)
    image_url = models.URLField(null=False, blank=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(null=False, blank=False, max_length=30)
    description = models.TextField(null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)
    type = models.CharField(null=False, blank=False, max_length=30)
