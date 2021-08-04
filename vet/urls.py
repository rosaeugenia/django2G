from django.urls import path

# Views
from .views import (
    # Pet owners
    PetOwnersListAPIView,
    PetOwnerRetrieve,
  # PetOwnersListCreateAPIView,
  # PetOwnerRetrieveUpdateDestroyAPIView,
  # #Pets
  PetListAPIView,
  # PetsListCreateAPIView,
  # PetRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Pet owners
    path("owners/", PetOwnersListAPIView.as_view(), name="owners_list"),
    path("owners/<int:pk>", PetOwnerRetrieve.as_view(), name="owners_retrieve"),
    
    path("pets/", PetListAPIView.as_view(), name="pets_list"),
    
# path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
# path( "owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(),
#     name="owners_retrieve-update-destroy"),
# #Pets
# path("pets/", PetsListCreateAPIView.as_view(), name="pets_list"),
# path( "pets/<int:pk>", PetRetrieveUpdateDestroyAPIView.as_view(),name="pets_retrieve-update-destroy"),
]
