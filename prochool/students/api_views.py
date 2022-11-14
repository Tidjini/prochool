from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models.establishment import Establishment
from .serializers import EstablishmentSerializer


class EstablishmentApiViewSet(viewsets.ModelViewSet):

    queryset = Establishment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EstablishmentSerializer
