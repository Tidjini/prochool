from django.db import models


class Establishment(models.Model):

    """Establishment for student:

    Ex: Colege, University:
    has students related_name in Student model
    """

    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255)
    # todo add others fileds for more details
