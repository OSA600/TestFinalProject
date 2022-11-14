from django.db import models


# Create your models here.
class Employees(models.Model):
    refAcces = models.CharField(max_length=50, default='here', blank=False)
    refOrdi = models.CharField(max_length=50, default='here', blank=False)
    refPhone = models.CharField(max_length=50, default='here', blank=False)
