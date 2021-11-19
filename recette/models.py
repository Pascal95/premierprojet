from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Recette(models.Model):
    nom_recette = models.CharField(max_length = 50)
    description_recette = models.TextField ()
    temps_recette = models.IntegerField()
    auteur_recette= models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="recette")
    def __str__(self): return self.nom_recette