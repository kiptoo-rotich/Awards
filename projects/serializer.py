from .models import Projects
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields='__all__'

