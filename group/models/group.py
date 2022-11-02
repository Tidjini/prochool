from django.db import models

from teacher.models import Teacher
from student.models import Student
from core.constants import DAYS_SEPARATER



class Group(models.Model):

    name = models.CharField(max_length=100)
    # days index separate by comma or other separater (, | ...)
    raw_days = models.CharField(max_length=13)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="groups")

    @property
    def days(self):
        return self.raw_days.split(DAYS_SEPARATER)



