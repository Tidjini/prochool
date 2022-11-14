from rest_framework import viewsets

from .models import Teacher
from .serializers import TeacherSerializer


class TeacherApiViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
