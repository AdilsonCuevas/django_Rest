from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers

class projectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers