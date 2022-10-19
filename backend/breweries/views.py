from django.shortcuts import render
from rest_framework import generics

from .models import Brewery
from .serializers import BrewerySerializer

#---------------------------------------------

class BreweryListCreateAPIView(generics.ListCreateAPIView):
    """
    Method for creating a brewery. TODO: only allow admin creation.
    """
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

    # takes in instance and serializer, later only allow admin
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        serializer.save()

brewery_list_create_view = BreweryListCreateAPIView.as_view()


class BreweryDetailAPIView(generics.RetrieveAPIView):
    """
    Method for viewing the details of a specific brewery.
    """
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    # lookup_field = 'pk' --> which field we want to do a lookup on
    # ie brewery.objects.get(pk=12)
