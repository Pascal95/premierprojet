from django.db import models
from django.contrib.auth import get_user_model
from recette.models import Recette
# Create your models here.

class Ingredient(models.Model):
    nom_ingredient = models.CharField(max_length = 50)
    quantite_ingredient = models.IntegerField()
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    
