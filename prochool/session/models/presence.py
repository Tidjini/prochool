from email.policy import default
from django.db import models



from .session import Session
from student.models import Student

class Presence(models.Model):

    
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='presences')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='my_presences')

    # difference between date of presence and session:
    # is that session can be started (or not yet),
    # and the student is presents in other session, 
    # and later then he will be related to his proper sessions. (Delays issues..)
    date = models.DateField(auto_now_add = True)


    # by defaults all student are absents
    absent = models.BooleanField(default=True)

    # to check if a student has an issue, and get checked out by an administrator
    by_admin = models.BooleanField()

    class Meta:
        ordering = 'date',