from rest_framework.decorators import api_view
from rest_framework.response import Response
from src.main import models
from . import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/universities',
        'GET /api/university/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getUniversities(request):
    products = models.Universities.objects.all()
    serializer = serializers.UniversitySerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUniversity(request, pk):
    product = models.Universities.objects.get(id=pk)
    serializer = serializers.UniversitySerializer(product, many=False)
    return Response(serializer.data)
