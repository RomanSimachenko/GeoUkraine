from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.IndexView, name="index"),

    path('api/', include('src.main.api.urls')),
]
