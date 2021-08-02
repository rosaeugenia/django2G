from vet.models import PetOwner
from rest_framework import serializers
from .models import PetOwner, Pet

class PetOwnerListSerializer(serializers.Serializer):
      id = serializers.IntegerField()
      first_name = serializers.CharField(max_length=255)
      last_name = serializers.CharField(max_length=255)
      
class PetOwnerSerializer(serializers.Serializer):
      id= serializers.ReadOnlyField()
      first_name = serializers.CharField(max_length=255)
      last_name = serializers.CharField(max_length=255)
      address = serializers.CharField()
      email = serializers.CharField()
      phone = serializers.CharField()      
      
      def create(self, validate_data):
            return PetOwner.objects.create(**validated_data)

class PetsListSerializer(serializers.Serializer):
      id = serializers.IntegerField()
      name = serializers.CharField(max_length=255)
      type = serializers.CharField(max_length=50)
      
      
class PetsDetailSerializer(serializers.Serializer):
      id= serializers.ReadOnlyField()
      name = serializers.CharField(max_length=255)
      type = serializers.CharField(max_length=50)