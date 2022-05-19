from rest_framework.serializers import ModelSerializer
from src.main import models


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = models.Universities
        fields = '__all__'
