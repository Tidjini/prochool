from django.db import models

from group.models import Group


class Session(models.Model):

    date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='sessions')
    open = models.BooleanField()

    class Meta:
        ordering = '-open', 'date'

