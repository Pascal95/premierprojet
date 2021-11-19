from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Recette
from recette.serializers.recette_serializer import AddRecetteSerializer
from recette.serializers.recette_serializer import RecetteSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.

class RecetteViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Recette.objects.all()
        serializer_class = RecetteSerializer(queryset, many=True)
        return Response(serializer_class.data, status=HTTP_200_OK)
    
    def post (self, request):
        serializers_class = AddRecetteSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=HTTP_200_OK)
        else:
            return Response(serializers_class.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        recette = Recette.objects.get(pk = pk)
        recette.delete()
        return Response(status = HTTP_200_OK)

    def retrieve(self,request,pk=None):
        queryset = Recette.objects.get(pk = pk)
        serializer_class = RecetteSerializer(queryset,many= False)
        return Response(serializer_class.data, status=HTTP_200_OK)
    
        
    