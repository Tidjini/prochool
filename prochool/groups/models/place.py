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
        # get student place
        return PlaceAPI.get_place(self.student, self.group)

    @property
    def empty(self):
        # empty if there is no student
        return bool(self.student)

    def save(self, *args, **kwargs):

        if self.pk:
            super().save(*args, **kwargs)
            return

        index = PlaceAPI.get_next_index(self.group)
        self.index = index
        super(Place, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("group", "student")
        ordering = ('index',)


class PlaceAPI:

    @staticmethod
    def get_place(student, group):
        '''Get Place by student or None'''
        try:
            return Place.objects.get(group=group, student=student)
        except Place.DoesNotExist:
            return None

    @staticmethod
    def get_next_index(group):
        '''Get next index, in given group'''
        return Place.objects.filter(group=group).count() + 1
