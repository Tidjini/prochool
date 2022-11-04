'''models for Payements application'''

from django.db import models
from prochool.students.models import Student
from prochool.teachers.models import Teacher

# Create your models here.


class Payment(models.Model):
    '''Payement: by envelope (printed by system) with unique Barre Code

    Each student and teacher has unique envelope for payment.
    We use Barre Code Scanner to confirme a payment transaction
    '''

    barre_code = models.CharField(max_length=13, primary_key=True)
    date = models.DateField(auto_now=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="payments")

    # Payment may not contain a Teacher
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, related_name='my_payments')

    amount = models.FloatField()

    # if payment is confirmed update Teacher Profile and Student Membership (use signals)
    confirmed = models.BooleanField()
    # to track if payment had insert by a user with a web form or by the Barre Code Scanner (Auto)
    manuel = models.BooleanField()
