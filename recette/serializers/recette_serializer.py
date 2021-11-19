from django.db.models import fields
from rest_framework import serializers
from recette.models import Recette


class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = serializers.ALL_FIELDS

class AddRecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = ('__all__')


