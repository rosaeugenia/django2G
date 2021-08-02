from django.urls import path
from django.urls.conf import path


#views

from .views import PetOwnersListCreate, PetsListCreate, PetOwnerDetailApiView, PetDetailApiView

urlpatterns = [
  path("owners/", PetOwnersListCreate.as_view(), name="owners_list"),
  path("pets/", PetsListCreate.as_view(), name="pets_list"),
  path("pets/<int:pk>",PetDetailApiView.as_view(), name="pet_detail"),
  path("owners/<int:pk>",PetOwnerDetailApiView.as_view(), name="owner_detail"),
]