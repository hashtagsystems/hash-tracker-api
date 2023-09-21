from rest_framework import serializers
from api.serializers.project_serializer import ProjectSerializer
from api.models import Category



class CategorySerializer(serializers.ModelSerializer):
    project=ProjectSerializer(many=True,read_only=True)
    class Meta:
        model=Project
        fields='__all__'