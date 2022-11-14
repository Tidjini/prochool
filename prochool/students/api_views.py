from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models.establishment import Establishment
from .models.parent import Parent
from .models.student import Student

from .serializers import EstablishmentSerializer, ParentSerializer, StudentSerializer


class EstablishmentApiViewSet(viewsets.ModelViewSet):

    queryset = Establishment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EstablishmentSerializer


class ParentApiViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (AllowAny,)


class StudentApiViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
