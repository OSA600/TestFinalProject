from django.db import models


# Create your models here.
class Employees(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateDeDemarrage = models.DateTimeField
    departement = models.CharField(max_length=50)
    lieu = models.CharField(max_length=50, default=None)
    natureDuPoste = models.CharField(max_length=50, default=None)
    refAcces = models.CharField(max_length=50, default=None)
    refOrdi = models.CharField(max_length=50, default=None)
    refPhone = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.nom, self.prenom, self.departement, self.dateDeDemarrage, self.dateDeDemarrage, self.lieu, self.natureDuPoste, self.refOrdi, self.refPhone, self.refAcces
