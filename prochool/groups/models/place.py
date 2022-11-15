from django.db import models


from .group import Group
from prochool.students.models import Student


class Place(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=10)
    # to set the exact place in our interface (presentation)
    index = models.IntegerField()
    # we can delete student but the place still thier
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, related_name='my_places')


    @property
    def place(self):
        return PlaceAPI.get_place(self.student, self.group)

    class Meta:
        unique_together = ("group", "student")
        ordering = ('index',)


class PlaceAPI:
   
    @staticmethod
    def get_place(student, group):
        try:
            _ = Place.objects.get(group=group, student=student)
            return _
        except Place.DoesNotExist:
            return None
