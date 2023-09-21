from rest_framework import serializers
from api.models import Project



class ProjectSerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Project
        fields='__all__'



