from rest_framework import serializers


from .models.establishment import Establishment
from .models.parent import Parent


# todo in details get students list of each establishment
class EstablishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establishment
        fields = '__all__'
        read_only = ('id',)


# todo in details get students of these parents
class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'
        read_only = 'id',
