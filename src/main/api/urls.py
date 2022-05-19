from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('universities/', views.getUniversities),
    path('university/<int:pk>/', views.getUniversity),
]
