from rest_framework import viewsets

from .serializer import CourseSerializer, PresenceSerializer
from .models.course import Course
from .models.presence import Presence


class CourseApiViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class PresenceApiViewSet(viewsets.ModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
