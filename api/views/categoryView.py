from rest_framework import generics
from api.models import Category
from api.serializers.category_serializer  import CategorySerializer

class CategoryList(generics.ListCreateAPIView):
        queryset=Category.objects.all()
        serializer_class=CategorySerializer