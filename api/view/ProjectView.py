from rest_framework import generics
from api.models import Project
from api.serializers.project_serializer  import ProjectSerializer
from rest_framework import permissions

class ProjectList(generics.ListCreateAPIView):
        # queryset=Category.objects.all()
        serializer_class=ProjectSerializer
        permission_classes=[permissions.IsAuthenticated]

        def  get_queryset(self):
                return Project.objects.all()