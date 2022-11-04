from django.db import models

from prochool.groups.models import Group


class Course(models.Model):

    date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='courses')
    open = models.BooleanField()

    class Meta:
        ordering = '-open', 'date'