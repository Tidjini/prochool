from rest_framework import viewsets

from .models.group import Group
from .models.place import Place

from .serializers import GroupSerializer, PlaceSerializer


# todo, in details, get: places
class GroupApiViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PlaceApiViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
