from rest_framework import serializes
from students.models import Establishment


class EstablishmentSerializer(serializes.ModelSerializer):

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only = ('id',)
