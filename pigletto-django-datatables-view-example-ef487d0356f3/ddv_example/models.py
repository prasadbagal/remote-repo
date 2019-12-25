from django.db import models

class TestModel(models.Model):
    first = models.CharField('first',default='', max_length = 10)
    last = models.CharField(max_length=10)
    mid = models.CharField(max_length=10)
    passw = models.CharField(max_length=10)
    name = models.CharField('Name', max_length=50, default='', blank=False)
    description = models.TextField('Description', default='')

    @property
    def testproperty(self):
        return '{} testprop'.format(self.name)
