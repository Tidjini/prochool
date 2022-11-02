from django.db import models


from teacher.models import Teacher
from .Student import Student


class Membership(models.Model):

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="my_memberships"
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, related_name="memberships_for"
    )

    remain_sessions = models.IntegerField()
    sessions = models.IntegerField()
    amount = models.FloatField()

    debit = models.FloatField()
    credit = models.FloatField()

    @property
    def balance(self) -> float:
        """Remains credits of a student"""

        return self.debit - self.credit

    @property
    def last_payement(self):
        pass

    @property
    def last_presence(self):
        pass

    @property
    def absences(self) -> int:
        return 0

    @property
    def absences_successif(self) -> int:
        """Absence Successif, to clear student after number of session given in configurations

        Ex: After 3 successif absence -> clear student from his group
        """
        return 0

    @property
    def free_sessions(self) -> int:
        return 0

    @property
    def free_sessions_successif(self) -> int:
        """Free sessions successif to determin student access after nomber successif of free session

        Ex: if student comes after 2 free session, admins will be notified to allow the student access or not
        """
        return 0

    class Meta:
        unique_together = ("student", "teacher")