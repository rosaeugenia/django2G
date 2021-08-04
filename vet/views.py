from rest_framework import generics

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerModelSerializer,
    PetOwnersListModelSerializer,
    #Pet
  PetModelSerializer,
  PetListModelSerializer,
  PetDateListModelSerializer,
  PetDateModelSerializer,    
)

# Models
from .models import PetOwner, Pet, PetDate


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer

    def get_queryset(self):

        first_name_filter = self.request.GET.get("first_name")
        filters = {}
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class
  

class PetListCreateAPIView(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer

    def get_queryset(self):

        pet_name_filter = self.request.GET.get("name")
        filters = {}
        if pet_name_filter:
            filters["name__icontains"] = pet_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetModelSerializer

        return serializer_class   
      
class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer


class PetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer    
  

class PetDateListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):

        pet_filter = self.request.GET.get("pet")
        filters = {}
        if pet_filter:
            filters["pet__icontains"] = pet_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetDateModelSerializer

        return serializer_class  

class PetDateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateModelSerializer    

def get_queryset(self):

        pet_name_filter = self.request.GET.get("pet")
        filters = {}
        if pet_name_filter:
            filters["pet__exact"] = pet_name_filter

        return self.queryset.filter(**filters)        



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
