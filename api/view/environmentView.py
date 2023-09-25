from rest_framework import generics
from api.serializers.environment_serializer import EnvironmentSerializer
from api.models import Environment

class EnvironmentListCreate(generics.ListCreateAPIView):
    serializer_class = EnvironmentSerializer

    def get_queryset(self):
        return Environment.objects.all()
    

class EnvironmentListDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()
    


