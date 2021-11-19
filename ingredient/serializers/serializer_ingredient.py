from rest_framework import serializers
from ingredient.models import Ingredient


class SerializerIngredient(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = serializers.ALL_FIELDS

class AddIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('__all__')


