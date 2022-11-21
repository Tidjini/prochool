from rest_framework import serializers


from .models.group import Group
from .models.place import Place
from prochool.students.serializers import StudentSerializer


class GroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = Group
        fields = '__all__'
        read_only_fields = 'id',


class PlaceSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(
        source='student', many=False, read_only=True)

    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = 'id',


class GroupDetailSerializer(serializers.ModelSerializer):

    places = PlaceSerializer(source='places', many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = 'id',
