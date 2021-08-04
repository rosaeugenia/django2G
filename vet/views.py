from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin


# Serializers
from .serializers import (
    # Pet Owner serializers
    PetListSerializer,
    PetOwnerSerializer,
    PetOwnerUpdateSerializer,
    PetOwnersListSerializer,
    PetOwnerRetrieveSerializer,
    # Pet serializers
    PetsListSerializer,
    PetSerializer,
    PetUpdateSerializer
)

# Models
from .models import PetOwner, Pet


class PetOwnersListAPIView(generics.ListAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListSerializer
    
 
class PetListAPIView(generics.ListAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetListSerializer   
    
    
class PetOwnerRetrieve(RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerRetrieveSerializer

  
    

#class PetOwnersListCreateAPIView(APIView):
#    """
#    View to list all pet owners in the system.
#    """
#    serializer_class = PetOwnersListSerializer
#    def get(self, request):
#        owners_queryset = PetOwner.objects.all()
#        serializer = self.serializer_class(owners_queryset, many=True)
#        return Response(data=serializer.data)
#    def post(self, request):
#        serializer = PetOwnerSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        created_instance = serializer.save()
#        serialized_instance = PetOwnerSerializer(created_instance)
#        return Response(serialized_instance.data, status=status.HTTP_201_CREATED)
#class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
#    """
#    View to retrieve owner by id.
#    """
#    serializer_class = PetOwnerSerializer
#    def get(self, request, pk):
#        owner = get_object_or_404(PetOwner, id=pk)
#        serializer = self.serializer_class(owner)
#        return Response(serializer.data)
#    def patch(self, request, pk):
#        owner = get_object_or_404(PetOwner, id=pk)
#        serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
#        serializer.is_valid(raise_exception=True)
#        updated_instance = serializer.save()
#        serialized_instance = self.serializer_class(updated_instance)
#        return Response(serialized_instance.data)
#    def delete(self, request, pk):
#        owner = get_object_or_404(PetOwner, id=pk)
#        owner.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#      
#class PetsListCreateAPIView(APIView):
#    """
#    View to list all pets in the system and create a pet.
#    """
#    serializer_class = PetsListSerializer
#    def get(self, request):
#        pets_queryset = Pet.objects.all()
#        serializer = self.serializer_class(pets_queryset, many=True)
#        return Response(data=serializer.data)
#    def post(self, request):
#      serializer = PetSerializer(data=request.data)
#      serializer.is_valid(raise_exception=True)
#      created_instance = serializer.save()
#      serialized_instance = PetSerializer(created_instance)
#      return Response(serialized_instance.data, status=status.HTTP_201_CREATED)
#    
#class PetRetrieveUpdateDestroyAPIView(APIView):
#      
#      """
#View to retrieve a pets by id.
#"""
#    
#serializer_class = PetSerializer
#def get(self, request, pk):
#        pet = get_object_or_404(Pet, id=pk)
#        serializer = self.serializer_class(pet)
#        return Response(serializer.data)
#def patch(self, request, pk):
#        pet = get_object_or_404(Pet, id=pk)
#        serializer = PetUpdateSerializer(instance=pet, data=request.data)
#        serializer.is_valid(raise_exception=True)
#        updated_instance = serializer.save()
#        serialized_instance = self.serializer_class(updated_instance)
#        return Response(serialized_instance.data)
#def delete(self, request, pk):
#        pet = get_object_or_404(Pet, id=pk)
#        pet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#      
