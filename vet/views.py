from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

#Models 
from .models import PetOwner, Pet
from .serializers import PetOwnerListSerializer, PetsListSerializer, PetOwnerSerializer,PetSerializer


class PetOwnersListCreate(APIView):
  """
  View to list all pet owners in the system.
  """
  
  serializer_class = PetOwnerListSerializer
  
  def get(self, request):
    
      owners_queryset = PetOwner.objects.all()
      serializer = self.serializer_class(owners_queryset, many=True)
      
      return Response(data=serializer.data)
  
  def post(self, request):

    serializer = PetOwnerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    created_instance = serializer.save()
    
    print(created_instance.__dict__)
    
    return Response({})
    


class PetsListCreate(APIView):
    """
    View to list all pets in the system.
    """

    serializer_class = PetsListSerializer

    def get(self, request):

        pets_queryset = Pet.objects.all()
        serializer = self.serializer_class(pets_queryset, many=True)
        return Response(data=serializer.data)
      
    def post(self, request):

      serializer = PetSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      created_instance = serializer.save()
    
      print(created_instance.__dict__)
    
      return Response({})  
    
