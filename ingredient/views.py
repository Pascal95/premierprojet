from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers, viewsets
from ingredient.serializers.serializer_ingredient import AddIngredientSerializer, SerializerIngredient
from ingredient.models import Ingredient
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Create your views here.

class IngredientViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Ingredient.objects.all()
        serializer_class = SerializerIngredient(queryset, many=True)
        return Response(serializer_class.data, status=HTTP_200_OK)

    def post(self,request):
        serializers_class = AddIngredientSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=HTTP_200_OK)
        else:
            return Response(serializers_class.errors, status=HTTP_400_BAD_REQUEST)

