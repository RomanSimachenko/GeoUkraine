from xml.etree.ElementInclude import include
from django.urls import path, include


urlpatterns = [
    path('api/', include('src.main.api.urls')),
]
