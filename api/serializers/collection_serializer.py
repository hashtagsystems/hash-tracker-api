from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Collection
        fields='__all__'


