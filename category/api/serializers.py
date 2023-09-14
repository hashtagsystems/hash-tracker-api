from rest_framework import serializers
from category.models import Category



class CategorySerializer(serializers.ModelSerializer):
    created_by=serializers.StringRelatedField(read_only=True)
    class Meta:
        model:Category
        fields='__all__'
