from rest_framework import serializers
from prochool.students.models import Establishment


class EstablishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only = ('id',)
