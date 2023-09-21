from rest_framework import generics
from api.models import Project
from api.serializers.project_serializer  import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
        # queryset=Category.objects.all()
        serializer_class=ProjectSerializer

        def  get_queryset(self):
                return Project.objects.all()