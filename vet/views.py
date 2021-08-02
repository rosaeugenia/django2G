from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404

#Models 
from .models import PetOwner, Pet
#Serializers
from .serializers import PetOwnerListSerializer, PetsListSerializer, PetOwnerSerializer, PetsDetailSerializer


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
  
class PetOwnerDetailApiView(APIView):

    serializer_class = PetOwnerSerializer

    def get(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)
      
      
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

      serializer = PetsListSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      created_instance = serializer.save()
    
      print(created_instance.__dict__)
    
      return Response({})
    
class PetDetailApiView(APIView):

    serializer_class = PetsDetailSerializer

    def get(self, request, pk):

      pet = get_object_or_404(Pet, id=pk)
      serializer = self.serializer_class(Pet)
      return Response(serializer.data)