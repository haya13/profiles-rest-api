from django.core.serializers import serialize
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing Hello APIView """
    name = serializers.CharField(max_length=10,min_length=2)
    email=serializers.EmailField(min_length=50)
    password=serializers.CharField(max_length=10)



