from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=30)


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    pets = models.ManyToManyField(Pet)  # Един Person може да има много pets или обратно
