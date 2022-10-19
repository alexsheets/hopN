# keep all brewery urls in this place
from django.urls import path

from . import views
#-----------------------------------------

# /api/breweries/
urlpatterns = [
    path('', views.brewery_list_create_view),
    path('<int:pk>/', views.BreweryDetailAPIView.as_view())
]