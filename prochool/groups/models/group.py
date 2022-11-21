from django.db import models


from prochool.teachers.models import Teacher
from prochool.core.constants import DAYS_SEPARATER


class Group(models.Model):

    name = models.CharField(max_length=100,)
    # days index separate by comma or other separater (, | ...)
    raw_days = models.CharField(max_length=13)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, related_name="groups")

    @property
    def days(self):
        return self.raw_days.split(DAYS_SEPARATER)

    class Meta:
        unique_together = ('name', 'teacher')
