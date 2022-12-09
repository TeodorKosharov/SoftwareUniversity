from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
