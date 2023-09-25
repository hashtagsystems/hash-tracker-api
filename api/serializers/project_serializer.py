from rest_framework import serializers
from api.models import Project
from api.serializers.environment_serializer import EnvironmentSerializer



class ProjectSerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField(read_only=True)
    environment=EnvironmentSerializer(many=True,read_only=True)
    class Meta:
        model=Project
        fields='__all__'



