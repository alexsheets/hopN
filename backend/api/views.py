from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

import json

from breweries.models import Brewery
from breweries.serializers import BrewerySerializer
#-------------------------------------------------------------

# django model instance to accomplish this response

@api_view(['POST'])
# @api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    api view for testing/simple tasks
    """
    serializer = BrewerySerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    else:
        return Response({"invalid": str(serializer.errors)}, status=400)

