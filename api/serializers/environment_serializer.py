from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Environment

class EnvironmentSerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Environment
        fields='__all__'
    