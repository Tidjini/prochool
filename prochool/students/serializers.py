from rest_framework import serializers


from .models.establishment import Establishment
from .models.parent import Parent


class EstablishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only = ('id',)


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'
        read_only = 'id',
