from datetime import datetime

# django
from django.db import models

# application
from prochool.groups.models import Group


class Course(models.Model):

    date = models.DateField(auto_now_add=True)
    closed_date = models.DateField()
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='courses')
    open = models.BooleanField(default=True)
    observation = models.CharField(max_length=255, null=True)

    def close(self):
        self.open = False
        self.closed_date = datetime.now().date()
        self.save()

    class Meta:
        ordering = '-open', 'date'


# open course, must close the old one then open new one

class CourseAPI:

    @staticmethod
    def get_by_group(group):
        try:
            return Course.objects.order_by('-open', 'date').get(group=group)
        except Course.DoesNotExist:
            return None

    @staticmethod
    def open(group):
        '''when open close old one, and create new course'''
        old = CourseAPI.get_by_group(group)
        if old:
            old.close()
        return Course.objects.create(group=group)


# close course, if new student subscribe to this course and not assist
