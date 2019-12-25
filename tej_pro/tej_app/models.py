from django.db import models

# Create your models here.


class MyModel(models.Model):
    first = models.CharField('first', max_length = 10)
    last = models.CharField('last', max_length=10)
    mid = models.CharField('mid', max_length=10)
    passw = models.CharField('passw', max_length=10)

    def __str__(self):
        return  self.first
