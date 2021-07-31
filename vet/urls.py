from django.urls import path
from django.urls.conf import path


#views

from .views import PetOwnersListCreate, PetsListCreate

urlpatterns = [
  path("owners/", PetOwnersListCreate.as_view(), name="owners_list"),
  path("pets/", PetsListCreate.as_view(), name="pets_list"),
]