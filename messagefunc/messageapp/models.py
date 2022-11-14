from django.db import models
from django.utils import timezone


# Create your models here.


class Employees(models.Model):
    nom = models.CharField(max_length=50, default=None)
    prenom = models.CharField(max_length=50, default=None)
    dateDeDemarrage = models.DateTimeField(default=timezone.now)
    departement = models.CharField(max_length=50, default=None)
    lieu = models.CharField(max_length=50, default=None)
    natureDuPoste = models.CharField(max_length=50, default=None)
    refAcces = models.CharField(max_length=50, default=None, null=False, blank=False)
    refOrdi = models.CharField(max_length=50, default=None, null=False, blank=False)
    refPhone = models.CharField(max_length=50, default=None, null=False, blank=False)

    def __str__(self):
        return self.nom, self.prenom, self.departement, self.dateDeDemarrage, self.dateDeDemarrage, self.lieu, self.natureDuPoste, self.refOrdi, self.refPhone, self.refAcces
