from django.db import models

# Create your models here.
class Enseignant(models.Model):
    nom = models.CharField(max_length=150)
    specialite = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Cours(models.Model):
    titre = models.CharField(max_length=300)
    description = models.TextField()
    credit = models.IntegerField()
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre