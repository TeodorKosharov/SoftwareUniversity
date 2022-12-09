from django.db import models


class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    age = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}, {self.age} years old'


class Task(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    priority = models.IntegerField(null=False, blank=False)
    assigned_to = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(blank=False, null=False, max_length=20)
    year = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(blank=False, null=False, max_length=20)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)


class Game(models.Model):
    title = models.CharField(null=False, blank=False, max_length=20)
    score = models.FloatField(null=False, blank=False)
    genre = models.CharField(null=False, blank=False, max_length=20)


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, max_length=20)
    profile_picture = models.ImageField(null=False, blank=False)

