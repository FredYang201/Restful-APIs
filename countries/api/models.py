from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=32)
    capital = models.CharField(max_length=64)
    population = models.CharField(max_length=128)
    area = models.CharField(max_length=128)
    continent = models.CharField(max_length=32)
    flag = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    currency = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)