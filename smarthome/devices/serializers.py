from rest_framework.serializers import ModelSerializer
from .models import Environment

class EnvironmentSerializer(ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'