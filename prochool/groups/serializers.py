from rest_framework import serializers


from .models.group import Group
from .models.place import Place


class GroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = Group
        fields = '__all__'
        read_only_fields = 'id',


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = 'id',
