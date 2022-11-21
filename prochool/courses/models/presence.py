from email.policy import default
from django.db import models


from .course import Course
from prochool.students.models import Student


class Presence(models.Model):

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='presences')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='my_presences')

    # difference between date of presence and session:
    # is that session can be started (or not yet),
    # and the student is presents in other session,
    # and later then he will be related to his proper sessions. (Delays issues..)
    date = models.DateField(auto_now_add=True)

    # by defaults all student are absents
    absent = models.BooleanField(default=True)

    # to check if a student has an issue, and get checked out by an administrator
    by_admin = models.BooleanField()

    @property
    def present(self):
        return PresenceAPI.present(self.student, self.group)

    class Meta:
        ordering = 'date',


'''Useful API for other places to call'''


class PresenceAPI:
    @staticmethod
    def get_last_presence(student, group):
        '''Get last Presence of student in Group

        return last presence in this group with absent property
        '''
        try:
            return Presence.objects.order_by('-date').get(student=student, group=group)

        except Presence.DoesNotExist:
            return None

    @staticmethod
    def present(student, group):
        last = PresenceAPI.get_last_presence(student, group)
        if last:
            return not last.absent
        return False

    @staticmethod
    def set_absent(student, group, course):
        last = PresenceAPI.get_last_presence(student, group)
        if last:
            last.absent = True
