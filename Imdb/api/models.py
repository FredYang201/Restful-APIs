from django.db import models
from .scrapy import Scrapy


class Movies(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=256)
    year = models.IntegerField()
    movieId = models.IntegerField()
    rate = models.FloatField()

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return '{}'.format(self.name)


