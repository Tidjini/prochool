from rest_framework import serializers

from .models.course import Course
from .models.presence import Presence


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = 'id',


class PresenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presence
        fields = '__all__'
        read_only_fields = 'id',
