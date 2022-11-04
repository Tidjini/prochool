from rest_framework import viewsets
from rest_framework.permisions import AllowAny
from students.models import Establishment
from students.serializers import EstablishmentSerializer


class EstablishmentApiViewSet(viewsets.ModelViewSet):

    queryset = Establishment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EstablishmentSerializer
