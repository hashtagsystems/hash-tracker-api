from rest_framework import generics
from api.serializers.collection_serializer import CollectionSerializer
from api.models import Collection

class collectionList(generics.ListCreateAPIView):
    serializer_class=CollectionSerializer

    def get_queryset(self):
        return Collection.objects.all()
    
class collectionListDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Collection.objects.all()
    serializer_class=CollectionSerializer
    
