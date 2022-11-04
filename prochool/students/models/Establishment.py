from django.db import models


class Establishment(models.Model):

    """Establishment for student:

    Ex: Colege, University:
    has students related_name in Student model
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    # todo add others fileds for more details
