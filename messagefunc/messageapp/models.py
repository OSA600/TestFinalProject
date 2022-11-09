from django.db import models
from django.utils import timezone

# Create your models here.
class Employees(models.Model):
    emp_id = models.ForeignKey(Employees, on_delete=models.PROTECT)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_de_demarrage = models.DateTimeField
    departement = models.CharField(max_length=50)

    def __str__(self):
        return self.nom, self.prenom, self.departement, self.date_de_demarrage, self.emp_id

