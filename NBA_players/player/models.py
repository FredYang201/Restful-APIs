from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.CharField(max_length=128)
    number = models.IntegerField()
    link = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    height = models.CharField(max_length=32)
    weight = models.CharField(max_length=32)
    born = models.CharField(max_length=32)
    age = models.CharField(max_length=16)
    years_in_nba = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'player'
        ordering = ('-created', )
