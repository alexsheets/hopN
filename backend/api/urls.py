from django.urls import path, include
from . import views
#---------------------------------

urlpatterns = [
    path('', views.api_home) # currently: localhost:8000/api
    # path('breweries/', include('breweries.urls'))
]