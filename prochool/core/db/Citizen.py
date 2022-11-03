from django.db import models


class Citizen(models.Model):
    """Citizen: Abstract Model containe:

    first & last name, phone, birthdate
    """

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    birthdate = models.DateField()

    class Meta:
        abstract = True
