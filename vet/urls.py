
from django.urls import path

# Views
from .views import (
    # Pet owners
    PetOwnersListCreateAPIView,
    PetOwnersRetrieveUpdateDestroyAPIView,
    #Pet
    PetListCreateAPIView,
    PetRetrieveUpdateDestroyAPIView,
    #Pet Date
    PetDateListCreateAPIView, 
    PetDateRetrieveUpdateDestroyAPIView
    
)

urlpatterns = [
    # Pet owners
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path(
        "owners/<int:pk>",
        PetOwnersRetrieveUpdateDestroyAPIView.as_view(),
        name="owners_retrieve-update-destroy",
    ),
    
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
    path(
        "pets/<int:pk>",
        PetRetrieveUpdateDestroyAPIView.as_view(),
        name="pets_retrieve-update-destroy",
    ),
    path("petdates/", PetDateListCreateAPIView.as_view(), name="petdates_list-create"),
    path(
        "petdates/<int:pk>",
        PetDateRetrieveUpdateDestroyAPIView.as_view(),
        name="petdates_retrieve-update-destroy",
    ),
    # path(
    #     "owners/<int:pk>",
    #     PetOwnerRetrieveUpdateDestroyAPIView.as_view(),
    #     name="owners_retrieve-update-destroy",
    # ),
]